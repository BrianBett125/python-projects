import json
import os
from datetime import datetime, timedelta

class Book:
    def __init__(self, id, title, author, isbn, copies=1):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.available_copies = copies

    def __str__(self):
        return f"ID: {self.id} | {self.title} by {self.author} (ISBN: {self.isbn}) | Copies: {self.available_copies}/{self.copies}"

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = {}  # book_id: due_date

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Email: {self.email}"

class Library:
    def __init__(self, data_file="library_data.json"):
        self.books = {}
        self.users = {}
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for book_data in data.get('books', []):
                    book = Book(book_data['id'], book_data['title'], book_data['author'], 
                              book_data['isbn'], book_data['copies'])
                    book.available_copies = book_data['available_copies']
                    self.books[book.id] = book
                for user_data in data.get('users', []):
                    user = User(user_data['id'], user_data['name'], user_data['email'])
                    user.borrowed_books = {int(k): datetime.fromisoformat(v) 
                                        for k, v in user_data['borrowed_books'].items()}
                    self.users[user.id] = user

    def save_data(self):
        data = {
            'books': [
                {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'isbn': book.isbn,
                    'copies': book.copies,
                    'available_copies': book.available_copies
                } for book in self.books.values()
            ],
            'users': [
                {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'borrowed_books': {str(k): v.isoformat() 
                                     for k, v in user.borrowed_books.items()}
                } for user in self.users.values()
            ]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def add_book(self, title, author, isbn, copies=1):
        book_id = max(self.books.keys(), default=0) + 1
        book = Book(book_id, title, author, isbn, copies)
        self.books[book_id] = book
        self.save_data()
        return book_id

    def add_user(self, name, email):
        user_id = max(self.users.keys(), default=0) + 1
        user = User(user_id, name, email)
        self.users[user_id] = user
        self.save_data()
        return user_id

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            return "User not found."
        if book_id not in self.books:
            return "Book not found."
        book = self.books[book_id]
        if book.available_copies <= 0:
            return "No copies available."
        
        user = self.users[user_id]
        if book_id in user.borrowed_books:
            return "User already borrowed this book."
        
        book.available_copies -= 1
        user.borrowed_books[book_id] = datetime.now() + timedelta(days=14)
        self.save_data()
        return f"Book borrowed successfully. Due date: {user.borrowed_books[book_id].strftime('%Y-%m-%d')}"

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            return "User not found."
        if book_id not in self.books:
            return "Book not found."
        
        user = self.users[user_id]
        if book_id not in user.borrowed_books:
            return "User hasn't borrowed this book."
        
        book = self.books[book_id]
        book.available_copies += 1
        due_date = user.borrowed_books[book_id]
        del user.borrowed_books[book_id]
        self.save_data()
        
        if datetime.now() > due_date:
            return f"Book returned successfully. Note: Book was overdue (due {due_date.strftime('%Y-%m-%d')})"
        return "Book returned successfully."

    def list_books(self):
        if not self.books:
            return "No books in library."
        return "\n".join(str(book) for book in self.books.values())

    def list_users(self):
        if not self.users:
            return "No users registered."
        return "\n".join(str(user) for user in self.users.values())

    def list_user_books(self, user_id):
        if user_id not in self.users:
            return "User not found."
        user = self.users[user_id]
        if not user.borrowed_books:
            return "No books borrowed by this user."
        result = "Borrowed books:\n"
        for book_id, due_date in user.borrowed_books.items():
            book = self.books[book_id]
            result += f"{book} (Due: {due_date.strftime('%Y-%m-%d')})\n"
        return result

def main():
    library = Library()
    print("Welcome to the Library Management System!")
    print("Commands: add_book, add_user, borrow, return, list_books, list_users, user_books, quit")

    while True:
        command = input("> ").lower().strip()
        if command == "quit":
            print("Thank you for using the Library Management System!")
            break
        
        if command == "add_book":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            copies = int(input("Enter number of copies: ") or 1)
            book_id = library.add_book(title, author, isbn, copies)
            print(f"Book added with ID {book_id}")

        elif command == "add_user":
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            user_id = library.add_user(name, email)
            print(f"User added with ID {user_id}")

        elif command == "borrow":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            print(library.borrow_book(user_id, book_id))

        elif command == "return":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            print(library.return_book(user_id, book_id))

        elif command == "list_books":
            print(library.list_books())

        elif command == "list_users":
            print(library.list_users())

        elif command == "user_books":
            user_id = int(input("Enter user ID: "))
            print(library.list_user_books(user_id))

        else:
            print("Invalid command. Available commands: add_book, add_user, borrow, return, list_books, list_users, user_books, quit")

if __name__ == "__main__":
    main()
