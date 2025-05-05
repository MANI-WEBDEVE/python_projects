class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")

b1= Book("1984", "George Orwell")
b2= Book("To Kill a Mockingbird", "Harper Lee")
b3= Book("The Great Gatsby", "F. Scott Fitzgerald")

print(b1.title)  # Output: 1984
print(b2.author)  # Output: Harper Lee
print(Book.total_books)  # Output: 3 (total books created)