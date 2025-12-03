class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        pass

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return super().__str__()

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return super().__str__()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            details = ""

            if isinstance(book, EBook):
                details = f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB"

            elif isinstance(book, PrintBook):
                details = f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}"

            else:
                details = f"Book: {book.title} by {book.author}"

            print(details)