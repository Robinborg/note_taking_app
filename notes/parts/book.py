
from database.connection import connect_database
from utils.insert_database import insert_db


class Books:
    def __init__(self):
        self.books_connection = connect_database(books = True)

    def insert_database(self):
        book_name = input("Enter book name:\n")
        book_review = input("Enter book review\n")
        insert_book = insert_db(write = book_name,
                                review = book_review)
        push_db = self.books_connection.insert_one(insert_book)
        return print(f"One insertion: {push_db.inserted_id}")
