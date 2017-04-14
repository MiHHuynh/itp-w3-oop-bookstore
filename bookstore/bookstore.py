class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def get_books(self):
        return self.books
    
    def add_book(self, book):
        self.books.append(book)
    
    def search_books(self, title=None, author=None):
        if (title != None and author == None):
            return [result for result in self.books if title.lower() in result.title.lower()]
        if (title == None and author != None):
            return [result for result in self.books if author == result.author]
        if (title != None and author != None):
            return [result for result in self.books if title in result.title and author == result.author]

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books
        
    def add_book(self, book):
        self.books.append(book)


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.author.add_book(self)
