'''
Features:

Add books to library

Display available books

Borrow a book (if available)

Return a book

Track borrowed books
'''
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed=True
            return True
        return False
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            return True
        return False
    
class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book): 
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def display_book(self):
        print("\nAvailable Books in Library:")
        available=[book for book in self.books if  not book.is_borrowed]  
        if not available:
            print("No Books available right now. ")
        else:
            for i ,book in enumerate(available,1):
                print(f"{i}.{book.title} by {book.author}") 

    def book_borrow(self,title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                 book.borrow()
                 print(f"You Borrowed'{book.title}'.Enjoy Reading !!!") 
                 return
        print("Sorry ,This book is unavailble .")

    def book_return(self,title):
        for book in self.books:
            if book.title.lower()==title.lower() and book.is_borrowed:
                book.return_book()
                print(f"'{book.title}' has been returned. Thank-You!!!!")
                return
            
            print("please enter valid name ")
    
def main():
    library=Library()
    library.add_book(Book("Python","john smith"))
    library.add_book(Book("Data structure","mark lee"))
    library.add_book(Book("ML","andrew ng"))

    while True:
        print("\n========Library Menu============")
        print("1.Display boook")
        print("2.Borrow Book")
        print("3.Return Book")
        print("4.Exit")
        choice=input("Enter Your Choice:")

        if choice=="1":
            library.display_book()
        elif choice=="2":
            title = input("Enter book title to borrow: ")

            library.book_borrow(title)

        elif choice=="3":
            title = input("Enter book title to return: ")
            library.book_return(title)

        elif choice == "4":
            print("Thanks for visiting the library!")  # exit message
            break
        else:
            print("Invalid choice. Try Again!!")

if __name__== "__main__" :
    main()





    
        

    
