class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(self.book_id, self.title, self.author, status)


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_issued = []

    def display(self):
        print(self.member_id, self.name, self.books_issued)


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        self.books[book_id] = Book(book_id, title, author)

    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Name: ")
        self.members[member_id] = Member(member_id, name)

    def lend_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")
        if book_id in self.books and member_id in self.members:
            book = self.books[book_id]
            if not book.is_issued:
                book.is_issued = True
                self.members[member_id].books_issued.append(book_id)
                print("Book issued")
            else:
                print("Book already issued")
        else:
            print("Invalid ID")

    def return_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")
        if book_id in self.books and member_id in self.members:
            book = self.books[book_id]
            if book.is_issued:
                book.is_issued = False
                if book_id in self.members[member_id].books_issued:
                    self.members[member_id].books_issued.remove(book_id)
                print("Book returned")
            else:
                print("Book was not issued")
        else:
            print("Invalid ID")

    def display_books(self):
        for book in self.books.values():
            book.display()


library = Library()

while True:
    print("\n1.Add Book\n2.Add Member\n3.Lend Book\n4.Return Book\n5.Display Books\n6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.add_member()
    elif choice == "3":
        library.lend_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        break
    else:
        print("Invalid choice")