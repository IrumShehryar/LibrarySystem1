

from library import Library

def main():
    lib = Library()

    print("\n📚 Welcome to the Library System")

    # Add books to the library
    lib.add_book("1984", "George Orwell")
    lib.add_book("The Hobbit", "J.R.R. Tolkien")

    print("\n📖 Books Added:")
    for book in lib.books:
        print(f"- {book.title} by {book.author} (Available: {book.available})")

    # Check availability
    print(f"\n🔍 Is '1984' available? {lib.is_available('1984')}")

    # Borrow a book
    print("\n📥 Borrowing '1984'...")
    success = lib.borrow_book("1984")
    print(f"Borrowed: {success}")
    print(f"Available now? {lib.is_available('1984')}")

    # Try borrowing it again
    print("\n📥 Trying to borrow '1984' again...")
    success = lib.borrow_book("1984")
    print(f"Borrowed: {success}")

    # Return the book
    print("\n📤 Returning '1984'...")
    returned = lib.return_book("1984")
    print(f"Returned: {returned}")
    print(f"Available now? {lib.is_available('1984')}")

    # Try returning again (already available)
    print("\n📤 Returning '1984' again...")
    returned = lib.return_book("1984")
    print(f"Returned: {returned}")

    # Borrow a non-existent book
    print("\n📥 Borrowing 'Unknown Book'...")
    success = lib.borrow_book("Unknown Book")
    print(f"Borrowed: {success}")

if __name__ == "__main__":
    main()

