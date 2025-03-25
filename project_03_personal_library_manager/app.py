import json

class PersonalLibrary:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_library()

    def load_library(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_library(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter publication year: ")
        genre = input("Enter book genre: ")
        read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        
        book = {
            "title": title,
            "author": author,
            "year": int(year),
            "genre": genre,
            "read": read_status
        }
        self.books.append(book)
        self.save_library()
        print("Book added successfully!\n")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.books = [book for book in self.books if book["title"].lower() != title.lower()]
        self.save_library()
        print("Book removed successfully!\n")

    def search_book(self):
        search_term = input("Enter book title or author to search: ").lower()
        results = [book for book in self.books if search_term in book["title"].lower() or search_term in book["author"].lower()]
        
        if results:
            print("\nSearch Results:")
            for book in results:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
        else:
            print("No books found.\n")

    def display_books(self):
        if not self.books:
            print("No books in the library.\n")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
        print()

    def display_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book["read"])
        read_percentage = (read_books / total_books * 100) if total_books > 0 else 0
        
        print(f"Total books: {total_books}")
        print(f"Books read: {read_books} ({read_percentage:.2f}% read)\n")

    def menu(self):
        while True:
            print("\nPersonal Library Manager")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.display_statistics()
            elif choice == "6":
                print("Exiting... Library saved.")
                break
            else:
                print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    library = PersonalLibrary()
    library.menu()
