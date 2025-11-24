# BOOK STORAGE

def save_book(book_id, title, author):
    with open("data/books.txt", "a") as file:
        file.write(f"{book_id},{title},{author}\n")

# Reads all books and returns a list of dict objects
def load_books():
    books = []
    try:
        with open("data/books.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                books.append({
                    "id": parts[0],
                    "title": parts[1],
                    "author": parts[2]
                })
    except FileNotFoundError:
        pass
    return books

# MEMBER STORAGE
def save_member(member_id, name):
    with open("data/members.txt", "a") as file:
        file.write(f"{member_id},{name}\n")

# Reads all members and returns a list of dict objects
def load_members():
    members = []
    try:
        with open("data/members.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                members.append({
                    "id": parts[0],
                    "name": parts[1]
                })
    except FileNotFoundError:
        pass
    return members

# ISSUE-RETURN STORAGE
def save_issue(book_id, member_id, date):
    with open("data/issued.txt", "a") as file:
        file.write(f"{book_id},{member_id},{date}\n")

# Reads issued records into a list of dict objects
def load_issued_books():
    issued_books = []
    try:
        with open("data/issued.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                issued_books.append({
                    "book_id": parts[0],
                    "member_id": parts[1],
                    "date": parts[2]
                })
    except FileNotFoundError:
        pass
    return issued_books


# Removes a book entry when it is returned
def remove_issue(book_id):
    issued = load_issued_books()
    updated = [entry for entry in issued if entry['book_id'] != book_id]

    # rewrite file
    with open("data/issued.txt", "w") as file:
        for entry in updated:
            file.write(f"{entry['book_id']},{entry['member_id']},{entry['date']}\n")
