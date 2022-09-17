from tests import (test_create_bookstore, test_add_get_authors,
                   test_add_get_books)
from bookstore import *


def run_tests():
    test_create_bookstore()
    test_add_get_authors()
    test_add_get_books()


def run_user_interface():
    options = {
        1: "Get bookstore's name",
        2: "Get a book by it's title",
        3: 'Get author from bookstore',
        4: "Get a book by it's author's name",
        5: 'Add new author to our list of authors',
        6: 'Add a new book to the book store',
        7: 'Leave the Best Library if you dare!'
    }
    functions = {
        1: Store_Name,
        2: book_by_title,
        3: Author_by_name,
        4: get_books_by_author_m,
        5: add_new_author,
        6: add_new_books,
        7: End_program
    }
    bookstore = new_BookStore()
    choice = 0
    while choice != 7:
        choice = Choice(options)
        functions[choice](bookstore)
        if choice != 7:
            print("\nbookstore's detalis so far:")
            print_bookstore(bookstore)
            print('\n')


def Store_Name(bookstore):
    print("The bookstore's name is: ", get_bookstore_name(bookstore))


def book_by_title(bookstore):
    book_title = wrong_typo("Enter book's title:")
    Book_information = get_book_by_title(bookstore, book_title)
    if Book_information is None:
        print("Book was not found in the Library")
    else:
        print("The book details are:")
        print(Book_information)


def Author_by_name(bookstore):
    name = wrong_typo("Enter author's name: ")
    author = get_author_by_name(bookstore, name)
    if author is None:
        print("Author was not found. ")
    else:
        print("author details: ")
        print(author + "")


def get_books_by_author_m(bookstore):
    author_name = wrong_typo('Enter books author:')
    if if_author_exists(bookstore, author_name) is True:
        Book_information = get_books_by_author(bookstore, author_name)
        print("The books information are: ")
        print(Book_information)
    else:
        print("Author was not found in our collection. ")


def add_new_author(bookstore):
    name = wrong_typo("Enter author's name:")
    nationality = wrong_typo("Enter author's Nationality: ")
    add_author(bookstore, name, nationality)
    print("Author added successfully thank you.")


def add_new_books(bookstore):
    title = wrong_typo("Enter book's title:")
    isbn = wrong_typo("Enter book's isbn:")
    if if_ISBN_exists(bookstore, isbn) is True:
        print("There is another book with the same ISBN code")
        print("Can't Add this book. ")
        return
    author_name = wrong_typo("Enter book's author:")
    if if_author_exists(bookstore, author_name) is True:
        add_book(bookstore, title, isbn, author_name)
        print("Book added successfully.")
    else:
        print("Author was not found in our collection.")
        print("please add the author to our Library.")


def lis_of_commands(lst):
    for i, dict in enumerate(lst):
        print(f"{i + 1})", end="")
        for k, v in dict.items():
            print(f"{k}={v}", end="")
        print()


def print_bookstore(bookstore):
    print('Bookstore name: ', get_bookstore_name(bookstore))
    authors = get_authors(bookstore)
    books = get_books(bookstore)
    if len(authors) == 0:
        print("No author found maybe he doesn't exist")
    else:
        print("Authors:")
        lis_of_commands(authors)
    if len(books) == 0:
        print(
            "No books found in our store today try again tomorrow\n mean while try going for something else"
        )
    else:
        print("Books:")
        lis_of_commands(books)


def wrong_typo(message):
    Inter_face = input(message + ' ')
    while len(Inter_face) == 0:
        print('Try again')
        Inter_face = input(message + ' ')
    return Inter_face


def new_BookStore():
    StoreName = wrong_typo(
        "Shhhhh you have just entered your bookstore what do you wish to call it: "
    )
    return create_bookstore(StoreName)


def Choice(options):
    possible_choices = list(options.keys())
    while True:
        for option in possible_choices:
            print(f'{option}) {options[option]}')
        try:
            choice = int(wrong_typo("Choose: "))
            if choice not in possible_choices:
                print('This option is not in the menu,try again')
            else:
                return choice
        except ValueError:
            print("Only number's are allowed")


def End_program(bookstore):
    print("ok, you choose to leave ", get_bookstore_name(bookstore),
          " book store.\nSee you Later :)")


run_tests()
run_user_interface()
