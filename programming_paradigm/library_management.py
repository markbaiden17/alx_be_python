class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f"Added book: '{book.title}'")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"SUCCESS: '{title}' has been checked out.")
                    return True
                else:
                    print(f"NOTICE: '{title}' is already checked out.")
                    return False
                
        print(f"ERROR: Book titled '{title}' not found in the library.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"SUCCESS: '{title}' has been returned.")
                    return True
                else:
                    print(f"NOTICE: '{title}' was already available.")
                    return False
                
        print(f"ERROR: Book titled '{title}' not found in the library.")
        return False

    def list_available_books(self):
        available_list = []
        for book in self._books:
            if book.is_available():
                available_list.append(str(book))
        
        if available_list:
            print("\n".join(available_list))
        else:
            print("No books are currently available.")