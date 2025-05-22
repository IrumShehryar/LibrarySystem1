
from library import Library

def main():
    lib = Library()
    lib.add_book("1984", "George Orwell")
    lib.add_book("The Hobbit", "J.R.R. Tolkien")

    print("Is '1984' available?", lib.is_available("1984"))
    lib.borrow_book("1984")
    print("Is '1984' available after borrowing?", lib.is_available("1984"))
    lib.return_book("1984")
    print("Is '1984' available after returning?", lib.is_available("1984"))

if __name__ == "__main__":
    main()
