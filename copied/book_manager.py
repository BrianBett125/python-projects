# Suggested filename: book_manager.py

class Book:
    """
    Represents a book with a title, author, and number of pages.
    This class demonstrates basic object-oriented programming concepts.
    """

    def __init__(self, title, author, pages):
        """
        The constructor method for the Book class.
        It's called automatically when a new Book object is created.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            pages (int): The number of pages in the book.
        """
        # Initialize the attributes of the Book object
        self.title = title
        self.author = author
        self.pages = pages
        print(f"A new book '{self.title}' has been created.")

    def get_info(self):
        """
        Returns a formatted string containing information about the book.

        Returns:
            str: A string with the book's title, author, and page count.
        """
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def is_long(self):
        """
        Checks if the book is considered 'long' (e.g., more than 500 pages).

        Returns:
            bool: True if the book has more than 500 pages, False otherwise.
        """
        return self.pages > 500

# --- Example Usage ---
if __name__ == "__main__":
    # Create instances (objects) of the Book class
    book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 193)
    book2 = Book("Dune", "Frank Herbert", 412)
    book3 = Book("War and Peace", "Leo Tolstoy", 1225)

    print("\n--- Book Information ---")
    # Access attributes and call methods on the objects
    print(book1.get_info())
    print(f"Is '{book1.title}' a long book? {book1.is_long()}")

    print(book2.get_info())
    print(f"Is '{book2.title}' a long book? {book2.is_long()}")

    print(book3.get_info())
    print(f"Is '{book3.title}' a long book? {book3.is_long()}")

    # You can also directly access attributes
    print(f"\nAuthor of book1: {book1.author}")
    book1.pages = 200 # Attributes can be modified
    print(f"Updated pages for '{book1.title}': {book1.pages}")

