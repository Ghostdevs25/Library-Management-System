[book.py](https://github.com/user-attachments/files/23727490/book.py)
from storage import *   
# BOOK MENU
# Shows the options related to books
def book_menu():
    while True:
        print("\n--- BOOK MANAGEMENT ---")
        print("1. Add a Book")
        print("2. Search Book by Title")
        print("3. Display All Books")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            display_books()
        elif choice == "4":
            break
        else:
            print("Invalid selection. Try again.")
# ADD BOOK
# Admin enters basic book details
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    # Save the book to storage
    save_book(book_id, title, author)

    print("Book added successfully!")
# SEARCH BOOK
# User can search by part of the title

def search_book():
    term = input("Enter title or keyword to search: ")
    books = load_books()
    found = False

    for book in books:
        if term.lower() in book['title'].lower():
            print(f"FOUND — ID: {book['id']} | Title: {book['title']} | Author: {book['author']}")
            found = True
    
    if not found:
        print("No matching book found.")
# DISPLAY BOOKS
# Shows every book stored in the system
def display_books():
    books = load_books()
    print("\n--- ALL BOOKS IN THE LIBRARY ---")

    if len(books) == 0:
        print("No books stored yet.")
        return

    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']}")
