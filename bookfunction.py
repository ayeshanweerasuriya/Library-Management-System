from classes import Book

def print_info(book):
    print(f"ISBN NO: {book.isbn_no}, Title: {book.title}, Format: {book.format}, Subject: {book.subject}, Rental price per day: {book.rental_price}, Number of Copies Available: {book.copies}")

class Book_Function:
    operation_cancelled = "Operation Cancelled"

    def __init__(self):
        self.list_of_books = []
        self.__initial_data()

    def __initial_data(self):
        book1 = Book(isbn_no="ISBN1231", title="Game Of Thrones", format="Hardcover", subject="Science", rental_price=12.50, copies=5)
        book2 = Book(isbn_no="ISBN1232", title="Vikings", format="Paperback", subject="History", rental_price=50.00, copies=0)
        book3 = Book(isbn_no="ISBN1234", title="The Great Gatsby", format="Hardcover", subject="Literature", rental_price=150.00, copies=2)
        self.list_of_books.append(book1)
        self.list_of_books.append(book2)
        self.list_of_books.append(book3)

    def add(self):
        __isnb = input("Enter ISBN Number:").strip().upper()
        #Check if isbn is already in the system
        for book in self.list_of_books:
            if __isnb == book.isbn_no:
                print(f"{__isnb} This isbn number is already in this system")
                return
            else:
                pass

        __title = input("Title:").strip().upper()
        __format = input("Format:")
        __subject = input("Subject:")

        # __rental_price = float(input("Rental price per day:"))
        try:
            __rental_price = int(input("Rental price per day:"))
        except ValueError:
            print("Invalid price entered, terminating...")
            return


        # __copies = int(input("Number of Copies Available:"))
        try:
            __copies = int(input("Copies: "))
        except ValueError:
            print("Invalid copies, Program terminating...")
            return

        book = Book(isbn_no=__isnb, title=__title, format=__format, subject=__subject, rental_price=__rental_price, copies=__copies)
        self.list_of_books.append(book)
        print(f"Book added {book.isbn_no}-{book.title}")

    def remove(self):
        __isbn = input("Enter ISBN number:")
        matched_data = list(x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            self.list_of_books.remove(x)
            print("Item Removed.")

    def lend(self):
        __isbn = input("Enter ISBN number:")
        __copies = int(input("Enter lend copies:"))
        matched_data = list(x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            x.copies -= __copies
            print("Book Lent")

    def receive(self):
        __isbn = input("Enter ISBN number:")
        __copies = int(input("Enter receive copies:"))
        matched_data = list(x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            x.copies += __copies
            print(f"Book Received with {__copies} Copies")

    # def display_all(self):
    #     for x in self.list_of_books:
    #         print_info(book=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_books if x.copies > 0)
        for x in matched_data:
            print_info(book=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_books if x.copies == 0)
        for x in matched_data:
            print_info(book=x)


