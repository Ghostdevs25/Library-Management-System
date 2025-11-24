from book import *
from member import *
from issue_return import *

def main_menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Book Management")
        print("2. Member Management")
        print("3. Issue / Return Books")
        print("4. Exit the system")

        choice = input("Choose an option: ")

        if choice == "1":
            book_menu()
        elif choice == "2":
            member_menu()
        elif choice == "3":
            issue_return_menu()
        elif choice == "4":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
