class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        print("List of books:")
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            title, author, _, _ = book.split(',')
            print(f"Title: {title}, Author: {author}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book release year: ")
        pages = input("Enter number of pages: ")
        self.file.write(f"{title},{author},{year},{pages}\n")
        print("Book added successfully")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        book_found = False
        for i, book in enumerate(books):
            if book.startswith(title + ','):
                del books[i]
                book_found = True
                break
        self.file.truncate(0)
        self.file.seek(0)
        for book in books:
            self.file.write(book + '\n')
        if book_found:
            print("Book removed successfully")
        else:
            print("Book not found")


lib = Library()

while True:
    print('\n' + "*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        del lib
        print("Exit successful.")
        break
    else:
        print("Invalid choice. Please try again.")
