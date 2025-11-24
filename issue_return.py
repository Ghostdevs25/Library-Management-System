from storage import *   
import datetime         
# ISSUE / RETURN MENU
# Shows all options related to borrowing & returning
def issue_return_menu():
    while True:
        print("\n--- ISSUE / RETURN MENU ---")
        print("1. Issue a Book to a Member")
        print("2. Return a Book")
        print("3. View All Issued Books")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            issue_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            display_issued_books()
        elif choice == "4":
            # Exit to main menu
            break
        else:
            print("Invalid option — please try again.")
            
# ISSUE BOOK
# Stores which member borrowed which book and when
def issue_book():
    print("\n--- ISSUE A BOOK ---")
    book_id = input("Enter the Book ID: ")
    member_id = input("Enter the Member ID: ")

    # Generate current date in YYYY-MM-DD format
    issue_date = datetime.date.today().strftime("%Y-%m-%d")

    save_issue(book_id, member_id, issue_date)
    print(" Book issued successfully!")

# RETURN BOOK
# Book comes back — we remove the issued entry
def return_book():
    print("\n--- RETURN A BOOK ---")
    book_id = input("Enter the Book ID: ")

    remove_issue(book_id)
    print(" Book returned successfully!")

# DISPLAY ALL ISSUED BOOKS
# Shows borrowed books with their member IDs and dates
def display_issued_books():
    issued_list = load_issued_books()
    print("\n--- LIST OF ISSUED BOOKS ---")

    if len(issued_list) == 0:
        print("No books are currently issued.")
        return

    for record in issued_list:
        print(f"Book ID: {record['book_id']} | Member ID: {record['member_id']} | Date: {record['date']}")

