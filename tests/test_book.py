from book import Book

def test_initialization():
    """Test 1: Initialization — title, author, and availability set correctly"""
    book = Book("Clean Code", "Robert Cecil Martin")
    assert book.title == "Clean Code"
    assert book.author == "Robert Cecil Martin"
    assert book.available is True

def test_borrow_when_available():
    """Test 2: Borrow when available — borrow() returns True, sets available to False"""
    book = Book("Clean Code", "Robert Cecil Martin")
    result = book.borrow()
    assert result is True
    assert book.available is False

def test_borrow_when_not_available():
    """Test 3: Borrow when not available — borrow() returns False, available remains False"""
    book = Book("Clean Code", "Robert Cecil Martin")
    book.borrow()  # First borrow
    result = book.borrow()  # Try borrowing again
    assert result is False
    assert book.available is False

def test_return_book():
    """Test 4: Return book — return_book() sets available to True"""
    book = Book("Clean Code", "Robert Cecil Martin")
    book.borrow()
    book.return_book()
    assert book.available is True
