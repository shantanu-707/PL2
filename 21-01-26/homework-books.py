class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def check_out(self):
        if self.available:
            print(f'Book: {self.book_name}')
            print(f'Author: {self.author}')
            confirm = input(f"Do you want to check out '{self.book_name}'? [Y/N]: ")

            if confirm.upper() == "Y":
                self.available = False
                name = input("Enter your name: ")
                print(f"{self.book_name} has been checked out by {name}.")
            else:
                print("Checkout cancelled.")
        else:
            print(f"'{self.book_name}' is currently not available.")

    def return_book(self):
        if not self.available:
            verify = input(f"Do you wish to return{self.book_name}? [Y/N]: ")
            if verify.upper() == "Y":
                self.available = True
                print(f"'{self.book_name}' has been returned.")
            if verify.upper() == "N":
                print("Let us know when you are done reading!")
        else:
            print(f"'{self.book_name}' was not checked out.")

    def display_book(self):
        if self.available:
            status = "Available"
        else:
            status = "Not available"
        print(f"Book: {self.book_name}, Author: {self.author}, Status: {status}")

book1 = Library("Python Programming", "Guido van Rossum")

book1.display_book()
book1.check_out()
book1.display_book()
book1.return_book()
book1.display_book()

