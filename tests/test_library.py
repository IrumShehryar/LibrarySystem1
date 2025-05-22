from library import Library

# 1. Library Initialization
def test_library_initialization():
    """
    Test: Library should initialize with an empty book list.
    """
    lib = Library()
    assert isinstance(lib.books, list)
    assert len(lib.books) == 0

# 2. Add book
def test_add_book():
    """
    Test: Add book to the library.
    - Book is added to the list with correct details.
    - Book is initially available.
    """
    lib = Library()
    lib.add_book("1984", "George Orwell")
    assert len(lib.books) == 1
    book = lib.books[0]
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.available is True

# 3. Check availability - exists
def test_is_available_true():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    assert lib.is_available("Dune") is True

# 4. Check availability - doesn’t exist
def test_is_available_false_for_nonexistent_book():
    lib = Library()
    assert lib.is_available("Nonexistent") is False

# 5. Borrow book - available
def test_borrow_book_available():
    lib = Library()
    lib.add_book("Clean Code", "Robert Martin")
    result = lib.borrow_book("Clean Code")
    assert result is True
    assert lib.books[0].available is False

# 6. Borrow book - already borrowed
def test_borrow_book_already_borrowed():
    lib = Library()
    lib.add_book("Clean Code", "Robert Martin")
    lib.borrow_book("Clean Code")
    result = lib.borrow_book("Clean Code")
    assert result is False
    assert lib.books[0].available is False

# 7. Borrow book - not in library
def test_borrow_book_not_in_library():
    lib = Library()
    result = lib.borrow_book("Unknown Book")
    assert result is False

# 8. Return book - valid
def test_return_book_valid():
    lib = Library()
    lib.add_book("Refactoring", "Martin Fowler")
    lib.borrow_book("Refactoring")
    result = lib.return_book("Refactoring")
    assert result is True
    assert lib.books[0].available is True

# 9. Return book - doesn’t exist
def test_return_book_not_in_library():
    lib = Library()
    result = lib.return_book("Nonexistent")
    assert result is False

# 10. Return book - already available
def test_return_book_already_available():
    """
    Returning a book that's already available:
    - Should return True.
    - Should not break logic.
    """
    lib = Library()
    lib.add_book("Domain-Driven Design", "Eric Evans")
    result = lib.return_book("Domain-Driven Design")
    assert result is True
    assert lib.books[0].available is True
