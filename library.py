class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if self.books:
            print("Available Books:")
            for i, book in enumerate(self.books, 1):
                if book.is_available:
                    print(f"{i}. {book}")
        else:
            print("No books available in the library.")

    def lend_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.is_available:
                print(f"You have borrowed {book}. Enjoy reading!")
                book.is_available = False
            else:
                print("Sorry, the book is currently not available.")
        else:
            print("Invalid book index.")

    def return_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if not book.is_available:
                print(f"Thank you for returning {book}.")
                book.is_available = True
            else:
                print("This book is already available in the library.")
        else:
            print("Invalid book index.")

def main():
    library = Library()

    # Adding some books to the library
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("1984", "George Orwell"))

    while True:
        print("\n===== Library Management System =====")
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            library.display_books()
            book_index = int(input("Enter the index of the book you want to borrow: "))
            library.lend_book(book_index)
        elif choice == '3':
            library.display_books()
            book_index = int(input("Enter the index of the book you want to return: "))
            library.return_book(book_index)
        elif choice == '4':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
