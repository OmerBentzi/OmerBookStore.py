from bookstore import (
    create_bookstore, get_bookstore_name, get_book_by_title,
    get_author_by_name, add_author, add_book, get_books_by_author)


def test_create_bookstore():
    store = create_bookstore("rmotr's bookstore")
    name = get_bookstore_name(store)
    assert name == "rmotr's bookstore"


def test_add_get_authors():
    store = create_bookstore("rmotr's bookstore")

    poe = add_author(store, 'Edgar Allan Poe', 'US')
    borges = add_author(store, 'Jorge Luis Borges', 'AR')
    joyce = add_author(store, 'James Joyce', 'UK')

    assert poe['name'] == 'Edgar Allan Poe'
    assert poe['nationality'] == 'US'

    assert borges['name'] == 'Jorge Luis Borges'
    assert borges['nationality'] == 'AR'

    assert joyce['name'] == 'James Joyce'
    assert joyce['nationality'] == 'UK'

    author = get_author_by_name(store, 'James Joyce')
    assert author['name'] == joyce['name']
    assert author['nationality'] == joyce['nationality']

    author = get_author_by_name(store, 'Edgar Allan Poe')
    assert author['name'] == poe['name']
    assert author['nationality'] == poe['nationality']


def test_add_get_books():
    store = create_bookstore("rmotr's bookstore")

    poe = add_author(store, 'Edgar Allan Poe', 'US')
    borges = add_author(store, 'Jorge Luis Borges', 'AR')
    joyce = add_author(store, 'James Joyce', 'UK')

    raven = add_book(store, 'The Raven', 'XXX-1', 'Edgar Allan Poe')
    ulysses = add_book(store, 'Ulysses', 'XXX-2', 'James Joyce')
    ficciones = add_book(store, 'Ficciones', 'XXX-3', 'Jorge Luis Borges')
    aleph = add_book(store, 'El Aleph', 'XXX-4', 'Jorge Luis Borges')

    book = get_book_by_title(store, 'The Raven')
    assert book['title'] == 'The Raven'
    assert book['isbn'] == 'XXX-1'
    assert book['author'] == 'Edgar Allan Poe'

    book = get_book_by_title(store, 'Ulysses')

    assert book['title'] == 'Ulysses'
    assert book['isbn'] == 'XXX-2'
    assert book['author'] == 'James Joyce'

    books = get_books_by_author(store, 'Jorge Luis Borges')
    assert len(books) == 2

    book1 = books[0]
    assert book1['title'] == 'Ficciones'
    assert book1['isbn'] == 'XXX-3'
    assert book1['author'] == 'Jorge Luis Borges'

    book2 = books[1]
    assert book2['title'] == 'El Aleph'
    assert book2['isbn'] == 'XXX-4'
    assert book1['author'] == 'Jorge Luis Borges'