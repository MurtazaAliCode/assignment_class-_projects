
import streamlit as st
import json

FILENAME = "library.json"

def load_library():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(books):
    with open(FILENAME, "w") as file:
        json.dump(books, file, indent=4)

def add_book(title, author, year, genre, read_status):
    books = load_library()
    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }
    books.append(book)
    save_library(books)

def remove_book(title):
    books = load_library()
    books = [book for book in books if book["title"].lower() != title.lower()]
    save_library(books)

def search_books(search_term):
    books = load_library()
    return [book for book in books if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]

def display_books():
    return load_library()

def display_statistics():
    books = load_library()
    total_books = len(books)
    read_books = sum(1 for book in books if book["read"])
    read_percentage = (read_books / total_books * 100) if total_books > 0 else 0
    return total_books, read_books, read_percentage

st.set_page_config(page_title="📚 Personal Library Manager", layout="wide")
st.title("📖 Personal Library Manager")

menu = st.sidebar.radio("Navigation", ["Add Book", "Remove Book", "Search Books", "View Library", "Statistics"])

if menu == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Have you read this book?")
    if st.button("Add Book"):
        if title and author and genre:
            add_book(title, author, year, genre, read_status)
            st.success(f"'{title}' has been added to your library!")
        else:
            st.error("Please fill in all fields.")

elif menu == "Remove Book":
    st.subheader("🗑️ Remove a Book")
    books = display_books()
    book_titles = [book["title"] for book in books]
    book_to_remove = st.selectbox("Select a book to remove", book_titles) if book_titles else None
    if book_to_remove and st.button("Remove Book"):
        remove_book(book_to_remove)
        st.success(f"'{book_to_remove}' has been removed from your library!")

elif menu == "Search Books":
    st.subheader("🔍 Search for a Book")
    search_query = st.text_input("Enter book title or author")
    if search_query:
        results = search_books(search_query)
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} {'✅ Read' if book['read'] else '❌ Unread'}")
        else:
            st.warning("No matching books found.")

elif menu == "View Library":
    st.subheader("📚 Your Library")
    books = display_books()
    if books:
        for book in books:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} {'✅ Read' if book['read'] else '❌ Unread'}")
    else:
        st.warning("Your library is empty. Add some books!")

elif menu == "Statistics":
    st.subheader("📊 Library Statistics")
    total_books, read_books, read_percentage = display_statistics()
    st.metric("Total Books", total_books)
    st.metric("Books Read", read_books)
    st.metric("Read Percentage", f"{read_percentage:.2f}%")