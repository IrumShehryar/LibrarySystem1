# LibrarySystem1

A simple Python library management system that allows you to add books, check availability, borrow, and return books.

## Features

- **Add Books:** Add books with title and author to the library.
- **Check Availability:** Check if a particular book is currently available.
- **Borrow Books:** Borrow a book from the library (marks it as unavailable).
- **Return Books:** Return a borrowed book (marks it as available again).

## Technologies

- Python 3.x
- No external dependencies required

## Project Structure

```
book.py         # Defines the Book class (title, author, available/borrow/return logic)
library.py      # Defines the Library class (manages a collection of Book objects)
main.py         # Example usage of the Library system
requirements.txt# (Optional/empty or generated file)
tests/          # Folder for test modules (if any)
```

## Example Usage

```python
from library import Library

lib = Library()
lib.add_book("1984", "George Orwell")
lib.add_book("The Hobbit", "J.R.R. Tolkien")

print("Is '1984' available?", lib.is_available("1984"))      # True
lib.borrow_book("1984")
print("Is '1984' available after borrowing?", lib.is_available("1984"))  # False
lib.return_book("1984")
print("Is '1984' available after returning?", lib.is_available("1984"))  # True
```

Or simply run:

```bash
python main.py
```

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/IrumShehryar/LibrarySystem1.git
    cd LibrarySystem1
    ```
2. (Optional) Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

## Dependencies

This project uses only standard Python 3 libraries and does **not** require any third-party packages.

## Testing

You can place your test scripts or modules inside the `tests/` folder.

