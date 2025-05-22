from book import Book

def test_initialization():
    book = Book("Clean Code", "Robert Martin")
    assert book.title == "Clean Code"
    assert book.author == "Robert Martin"
    assert book.available is True

def test_borrow_when_available():
    book = Book("Clean Code", "Robert Martin")
    assert book.borrow() is True
    assert book.available is False

def test_borrow_when_unavailable():
    book = Book("Clean Code", "Robert Martin")
    book.borrow()
    assert book.borrow() is False

def test_return_book():
    book = Book("Clean Code", "Robert Martin")
    book.borrow()
    book.return_book()
    assert book.available is True
