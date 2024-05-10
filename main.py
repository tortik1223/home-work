import random
import string
my_book = 'book'

def generate_number(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def log(masenge):
    with open(my_book, 'a' ,encoding='utf-8') as file:
        file.write(masenge + '\n')



class Book:

    def __init__(self, title, author="", is_available=True):
        self.title = title
        self.author = author
        self.isbn = generate_number()
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            log('книга взята')
            self.is_available = False
        else:
            print("No book")

    def return_book(self):
        self.is_available = True
        log('вернули книгу')

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        log('добавили книгу')
    def list_available_books(self):
        for book in self.books:
            print(book.title)
            log('инфа. про автор')
            if not book.is_available:
                print('the book is not there')
            else:
                print("present.")


book1 = Book(title='The Violet and the Tom', author='Eve Ocotillo')

print(book1.title)
print(book1.author)
print(book1.isbn)
print(book1.is_available)

book1.borrow()

print(book1.is_available)

book1.return_book()

print(book1.is_available)

library = Library()

library.add_book(book1)

library.list_available_books()

log