# Task 1: Library System Enhancement 
# Sharpen your skills in managing and modifying data within tuples and lists.
# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this 
# system by adding new books and ensuring no duplicates.
# Existing Library Data:
# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def add_book():
    book_title = str(input("What is the name of the book you would like to add to the library?: "))
    book_author = str(input("Who is the author of the book?: "))
    book_add = (book_title, book_author)
    if book_add in library:
        print("That book already exists in the library.")
    else:
        library.append(book_add)
        print(library)

# V2
for index, (name, departure, arrival) in enumerate(itinerary):
    print(f"{index + 1}: {name} - From {departure} to {arrival}")
    


while True:
    user_input = input("Would you like to add a new book to the library? (yes/no): ").lower()
    if user_input == "yes":
        add_book()
    else:
        break