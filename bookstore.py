def create_bookstore(name):
  return {'name': name, 'lastauthorid': 1, 'lastbookid':1, 'books' : [], 'authors' : []}
    
 
def get_bookstore_name(bookstore):
  return bookstore['name']


def add_author(bookstore, name, nationality):
    newauthor = {'name': name, 'nationality': nationality, 'id': 
    bookstore['lastauthorid']}
    bookstore['authors'].append(newauthor)
    bookstore['lastauthorid'] += 1
    return newauthor
   


def get_author_by_name(bookstore, name):
  for books in bookstore['authors']:
        if books['name'] == name:
            return books

def get_authors(bookstore):
    return bookstore['authors']

  
def add_book(bookstore, title, isbn, author):
    newbook = {'isbn' : isbn, 'title' : title, 'author' : 
    author, 'id' : bookstore['lastbookid']}
    bookstore['books'].append(newbook)
    bookstore['lastbookid'] += 1
    return newbook
  

def get_book_by_title(bookstore, title):
   for books in bookstore['books']:
        if books['title'] == title:
            return books
  

def get_books(bookstore):
    return bookstore['books']

  
def get_books_by_author(bookstore, author):
  booklist =[]
  for book in bookstore['books']:
     if book['author'] == author:
            booklist.append(book)
       
  return booklist


def if_ISBN_exists(bookstore, isbn):
    for book in bookstore['books']:
        if book['isbn'] == isbn:
            return True
    return False


def if_author_exists(bookstore, author_name):
    for author in bookstore['authors']:
        if author['name'] == author_name:
            return True
    return False
