from classes import Magazine


def print_info(magazine):
    print(
        f"Magazine Number: {magazine.m_no}, Title: {magazine.title}, Format: {magazine.color}, Subject: {magazine.subject}, Rental Price: {magazine.rental_price}, Available Copies:{magazine.copies}")


class Magazine_Function:

    def __init__(self):
        self.list_of_magazines = []
        self.__initial_data()

    def __initial_data(self):
        a_magazine1 = Magazine(m_no="01", title="National Geographic", color="Blue", subject="Science",
                               rental_price=120.50, copies=1)
        a_magazine2 = Magazine(m_no="02", title="The New Yorker", color="Black & White", subject="Technology",
                               rental_price=220.50, copies=4)
        a_magazine3 = Magazine(m_no="03", title="Time", color="Format3", subject="Sports", rental_price=30.50, copies=5)
        self.list_of_magazines.append(a_magazine1)
        self.list_of_magazines.append(a_magazine2)
        self.list_of_magazines.append(a_magazine3)

    def add(self):
        __mnum = input("Enter Magazine Number:").strip().upper()

        for magazine in self.list_of_magazines:
            if __mnum == magazine.m_no:
                print(f"{__mnum} This m number is already in this system")
                return
            else:
                pass

        __title = input("Title:").strip().upper()
        __color = input("Color:")
        __subject = input("Subject:")

        try:
            __rental_price = int(input("Rental price per day:"))
        except ValueError:
            print("Invalid price entered, terminating...")
            return

        try:
            __copies = int(input("Copies: "))
        except ValueError:
            print("Invalid copies, Program terminating...")
            return

        a_magazine = Magazine(m_no=__mnum, title=__title, color=__color, subject=__subject, rental_price=__rental_price,
                              copies=__copies)
        self.list_of_magazines.append(a_magazine)
        print(f"Magazine Added {a_magazine.m_no}-{a_magazine.title}")

    def remove(self):
        __mnum = input("Enter Magazine Number:")
        matched_data = list(x for x in self.list_of_magazines if x.m_no == __mnum)
        for x in matched_data:
            self.list_of_magazines.remove(x)
            print("Item Removed.")

    def lend(self):
        __mnum = input("Enter Magazine Number:")
        __copies = int(input("Enter Lend Copies:"))
        matched_data = list(x for x in self.list_of_magazines if x.m_no == __mnum)
        for x in matched_data:
            x.copies -= __copies
            print("Magazine Lent")

    def receive(self):
        __mnum = input("Enter Magazine Number:")
        __copies = int(input("Enter Receive Copies:"))
        matched_data = list(x for x in self.list_of_magazines if x.m_no == __mnum)
        for x in matched_data:
            x.copies += __copies
            print(f"Magazine Received With {__copies} Copies")

    def display_available(self):
        matched_data = list(x for x in self.list_of_magazines if x.copies > 0)
        for x in matched_data:
            print_info(magazine=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_magazines if x.copies == 0)
        for x in matched_data:
            print_info(magazine=x)
