from storage import *   
# MEMBER MENU
# Shows options for managing members
def member_menu():
    while True:
        print("\n--- MEMBER MANAGEMENT ---")
        print("1. Register a New Member")
        print("2. View All Members")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            display_members()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")
# ADD MEMBER
# Admin enters member details
def add_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")

    save_member(member_id, name)
    print("Member added successfully!")
# DISPLAY MEMBERS
# Lists all registered members
def display_members():
    members = load_members()
    print("\n--- REGISTERED MEMBERS ---")

    if len(members) == 0:
        print("No members found.")
        return

    for member in members:
        print(f"ID: {member['id']} | Name: {member['name']}")
