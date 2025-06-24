# online book store management system
# using OOPs 
book_list = []
def display_books(book_list):
    """
    Displays the list of books.
    
    :param book_list: List of books
    """
    if not book_list:
        print("No books available.")
        return
    
    print("Available Books:")
    for book in book_list:
        print(f"Title: {book['title']}, Author: {book['author']}, Price: {book['price']}")
def add_book(book_list, book):
    """
    Adds a book to the book list.
    
    :param book_list: List of books
    :param book: Book to be added
    """
    book_list.append(book)
    print(f"Book '{book['title']}' added successfully.")

def remove_book(book_list, book):
    """
    Removes a book from the book list.

    :param book_list: List of books
    :param book: Book to be removed
    """
    if book in book_list:
        book_list.remove(book)
        print(f"Book '{book['title']}' removed successfully.")
    else:
        print(f"Book '{book['title']}' not found in the list.")
def search_book(book_list, title):
    """
    Searches for a book by title in the book list.

    :param book_list: List of books
    :param title: Title of the book to search for
    :return: Book if found, else None
    """
    for book in book_list:
        if book['title'].lower() == title.lower():
            return book
    return None
def update_book(book_list, title, new_details):
    """Updates the details of a book in the book list.
    :param book_list: List of books
    :param title: Title of the book to update
    :param new_details: Dictionary containing the updated details
    """
    book = search_book(book_list, title)
    if book:
        book.update(new_details)
        print(f"Book '{title}' updated successfully.")
    else:
        print(f"Book '{title}' not found in the list.")
def main():
    while True:
        print("\nBook Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Update Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_books(book_list)
        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            add_book(book_list, {'title': title, 'author': author, 'price': price})
        elif choice == '3':
            title = input("Enter book title to remove: ")
            book = search_book(book_list, title)
            if book:
                remove_book(book_list, book)
            else:
                print(f"Book '{title}' not found.")
        elif choice == '4':
            title = input("Enter book title to search: ")
            book = search_book(book_list, title)
            if book:
                print(f"Found Book - Title: {book['title']}, Author: {book['author']}, Price: {book['price']}")
            else:
                print(f"Book '{title}' not found.")
        elif choice == '5':
            title = input("Enter book title to update: ")
            new_title = input("Enter new title (leave blank to keep current): ")
            new_author = input("Enter new author (leave blank to keep current): ")
            new_price = input("Enter new price (leave blank to keep current): ")
            
            new_details = {}
            if new_title:
                new_details['title'] = new_title
            if new_author:
                new_details['author'] = new_author
            if new_price:
                new_details['price'] = float(new_price)
                
            update_book(book_list, title, new_details)
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()