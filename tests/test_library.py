from library import Library

def test_add_book():
    lib = Library()
    lib.add_book("1984", "George Orwell")
    assert len(lib.books) == 1

def test_is_available_true():
    lib = Library()
    lib.add_book("1984", "George Orwell")
    assert lib.is_available("1984")

def test_borrow_book_success():
    lib = Library()
    lib.add_book("1984", "George Orwell")
    assert lib.borrow_book("1984")
    assert not lib.books[0].available

def test_return_book_success():
    lib = Library()
    lib.add_book("1984", "George Orwell")
    lib.borrow_book("1984")
    assert lib.return_book("1984")
