class Book:
    def __init__(self, title, author, genre, rating):
        # Constructor to initialize a book with title, author, genre, and rating.
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating
    
    def display_book_details(self):
        # Method to display the book details.
        #we can use either , or + to concatenate string and variable
        print("TITLE :" , self.title) 
        print("AUTHOR :" + self.author)


# Example usage:
book1 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 5)
book1.display_book_details()

