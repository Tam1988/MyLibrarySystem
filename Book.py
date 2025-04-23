class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.read = False

    def read_book(self):
        if not self.read:
            self.read = True
            return f"You have read '{self.title}' by {self.author}."
        return f"You have already read this book '{self.title}', try other books written by '{self.author}'."

    def unread_book(self):
        if self.read:
            self.read = False
            return f"You have not read '{self.title}' by {self.author}."
        return f"You have not read this book '{self.title}' by '{self.author}'."

    def get_details(self):
        return f"Title: {self.title} by Author: {self.author}, Year: {self.year}, Read: {self.read}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [book.get_details() for book in self.books]

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None        

class Ebook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def stream(self):
        return f"Streaming '{self.title}' by {self.author}. File size: {self.file_size}MB."

    def read_book(self):
        return f"'{self.title}' is an Ebook. Get a Kindle subscription to enjoy streaming it anytime!"

class Audiobook(Book):
    def __init__(self, title, author, year, duration):
        super().__init__(title, author, year)
        self.duration = duration

    def listen(self):
        return f"Listening to '{self.title}' by {self.author}. Duration: {self.duration} hours."

    def read_book(self):
        return f"'{self.title}' is an Audiobook. Plug in your device and enjoy listening!"
