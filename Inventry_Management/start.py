'''

Inventory Management System

📦 Concepts: File handling + OOP.

Add, update, delete products.

Each product → ID, name, stock, price.

Save inventory to a file (so it persists after closing program).

Search products by name/ID.
'''

import json

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Qty: {self.quantity}, Price: {self.price}"

class Inventory:
    def __init__(self):
        self.products = []
        self.load_data()

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added successfully!!")
        self.save_data()

    def display_product(self):
        if not self.products:
            print("No Products in inventory!!!!!")   
        else:
            print("Inventory List:") 
            for product in self.products:
                print(product)

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def update_product(self, product_id, new_qty=None, new_price=None):
        product = self.search_product(product_id)
        if product:
            if new_qty is not None:
                product.quantity = new_qty
            if new_price is not None:
                product.price = new_price
            print(f"Product: '{product.name}' Updated Successfully!!!")
            self.save_data()
        else:
            print("Product Not Found.")

    def delete_product(self, product_id):
        product = self.search_product(product_id)
        if product:
            self.products.remove(product)
            print(f"Product '{product.name}' deleted Successfully!!!")
            self.save_data()
        else:
            print("Product Not Found")

    def save_data(self):
        data = [vars(product) for product in self.products]
        with open("inventory.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open("inventory.json", "r") as f:
                data = json.load(f)
                self.products = [Product(**item) for item in data]
        except FileNotFoundError:
            self.products = []

def main():
    inventory = Inventory()

    while True:
        print("\n============INVENTORY MENU=============")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            pid = input("Enter Product ID: ")
            name = input("Enter Product name: ")
            qty = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            inventory.add_product(Product(pid, name, qty, price))

        elif choice == "2":
            inventory.display_product()

        elif choice == "3":
            pid = input("Enter Product ID to Search: ")
            product = inventory.search_product(pid)
            if product:
                print("Found:", product)
            else:
                print("Product Not Found.")
            
        elif choice == "4": 
            pid = input("Enter Product ID to Update: ")
            qty = input("Enter New Quantity (leave blank to skip): ")
            price = input("Enter New Price (leave blank to skip): ")

            inventory.update_product(
                pid,
                int(qty) if qty else None,
                float(price) if price else None 
            )

        elif choice == "5":
            pid = input("Enter Product ID to delete: ")
            inventory.delete_product(pid)

        elif choice == "6":
            print("Exiting Inventory System. Goodbye!!")
            break
        else:
            print("Invalid Choice! Try again.")

if __name__ == "__main__":
    main()
