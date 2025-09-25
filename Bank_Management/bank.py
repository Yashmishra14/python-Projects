#Dictionary to store details 

accounts={}

# Function to create a new account
def create_acc():
    name=input('Enter your name:')
    acc_no=input('Enter Account number:')
    if acc_no in accounts:
        print("account already exists!")
        return
    balance=float(input("Enter initial Deposit: "))
    accounts[acc_no]={"name":name,'balance':balance}
    print(f'Account created successfully for name{name} with balance {balance}')


# Function to display account details

def display_acc():
    acc_no=input('Enter Account number:')
    if acc_no in accounts:
        print(f'name:{accounts[acc_no]['name']}')
        print(f'Balance:{accounts[acc_no]['balance']}')
    else:
        print('Account Not found!')

def deposite():
    acc_no=input("Enter Account Number:")
    if acc_no in accounts:
        amount=float(input('Enter amount to deposite:'))
        accounts[acc_no]['balance']+=amount
        print(f'Amount deposited succesfully .New Balance:{accounts[acc_no]['balance']}')
    else:
        print("Account Not found ")

# Function to withdraw money

def withdraw():
    acc_no=input('Enter account Number:')
    if acc_no in accounts:
        amount=float(input('Enter withdraw ammount'))
        if accounts[acc_no]['balance']>=amount:
            accounts[acc_no]['balance']-=amount
            print(f"Amount withdrawn successfully. New balance: {accounts[acc_no]['balance']}")
        else:
            print("Insufficient Balance")

    else:
        print('Account Not found!!!')

def main():
    while True:
        print("\n=== BANK MANAGEMENT SYSTEM ===")
        print("1. Create Account")
        print("2. Display Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_acc()
        elif choice == '2':
            display_acc()
        elif choice == '3':
            deposite()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            print("Thank you for using our bank system!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()




