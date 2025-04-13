import json
import os

def main():
    # Main function to display menu and handle user choices.

    def add_book():
        # Adds a new book to the library and saves it to the JSON file.
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter publication year: ")
        gener= input("Enter book genre: ")
        read = input("Have you read this book? (yes/no): ").lower()
        if read not in ['yes', 'no']:
            print("Invalid input, please enter 'yes' or 'no'.")
            return
        new_book = {"title": title, "author": author, "year": year, "genre": gener, "read": read}
        
        if os.path.exists('library_data.json'):
            with open('library_data.json', 'r') as f:
                library = json.load(f)
        else:
            library = []

        library.append(new_book)

        with open('library_data.json', 'w') as f:
            json.dump(library, f, indent=4)
        print(f"Book '{title}' added to the library.")

    def view_books():
        # Displays all books in the library.
        if not os.path.exists('library_data.json'):
            print("No books in the library.")
            return
        if os.path.getsize('library_data.json') == 0:
            print("No books in the library.")
            return
        print("Books in the library:")
        with open('library_data.json', 'r') as f:
            library = json.load(f)
        for book in library:
            print(f"Book {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {book['read']}")

    def search_book():
        # Searches for books in the library by title.
        title=input("Enter the title of the book to search: ")
        with open('library_data.json', 'r') as f:
            library = json.load(f)
        if not library:
            print("No books in the library.")
            return
        found_books = [book for book in library if title.lower() in book["title"].lower()]
        if not found_books:
            print(f"No books found with title containing '{title}'.")
            return
        print("Books found:")
        for i, book in enumerate(found_books, 1):
           
            read_status = "Read" if book["read"] == "yes" else "Not Read"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - {read_status}")

    def remove_book():
        # Removes a book from the library by title.
        title = input("Enter the title of the book to remove: ")
        with open('library_data.json', 'r') as f:
            library = json.load(f)
        if not library:
            print("No books in the library.")
            return
        for book in library:
            if book["title"].lower() == title.lower():
                library.remove(book)
                print(f"Book '{title}' removed from the library.")
                with open('library_data.json', 'w') as f:
                    json.dump(library, f, indent=4)
                return
        print(f"No book found with title '{title}'.")

    def show_statistics():
        # Displays statistics about the library (total books, read/unread books, etc.).
        if not os.path.exists('library_data.json'):
            print("No books in the library.")
            return
        with open('library_data.json', 'r') as f:
            library = json.load(f)
        total_books = len(library)
        read_books = len([book for book in library if book["read"] == "yes"])
        unread_books = total_books - read_books
        print(f"Total books: {total_books}")
        print(f"Books read: {read_books}")
        print(f"Books not read: {unread_books}")
        print(f"Books read percentage: {read_books / total_books * 100:.2f}%") if total_books > 0 else print("No books to calculate statistics.")
    
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            remove_book()
        elif choice == '5':
            show_statistics()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
