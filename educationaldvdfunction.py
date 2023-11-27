from classes import Educational_DVD

def print_info(educational_dvd):
    print(f"Educational_DVD NO: {educational_dvd.dvd_no}, Title: {educational_dvd.title}, Subject: {educational_dvd.subject}, Rental Price: {educational_dvd.rental_price}, Available Copies:{educational_dvd.copies}")

class Educational_DVD_Function:

    def __init__(self):
        self.list_of_educational_dvds = []
        self.__initial_data()

    def __initial_data(self):
        a_educational_dvd1 = Educational_DVD(dvd_no="10", title="Planet Earth", subject="Astronomy", rental_price=120.50, copies=10)
        a_educational_dvd2 = Educational_DVD(dvd_no="11", title="The History of Maths", subject="Math", rental_price=220.50, copies=0)
        a_educational_dvd3 = Educational_DVD(dvd_no="12", title="The Human Body", subject="Technology", rental_price=320.50, copies=5)
        self.list_of_educational_dvds.append(a_educational_dvd1)
        self.list_of_educational_dvds.append(a_educational_dvd2)
        self.list_of_educational_dvds.append(a_educational_dvd3)

    def add(self):
        __dvd_no = input("Enter Educational DVD Number:").strip().upper()

        for educational_dvd in self.list_of_educational_dvds:
            if __dvd_no == educational_dvd.dvd_no:
                print(f"{__dvd_no} This dvd number is already in this system")
                return
            else:
                pass

        __title = input("Title:").strip().upper()
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

        a_educational_dvd = Educational_DVD(dvd_no=__dvd_no, title=__title, subject=__subject, rental_price=__rental_price, copies=__copies)
        self.list_of_educational_dvds.append(a_educational_dvd)
        print(f"Educational DVD Added {a_educational_dvd.dvd_no}-{a_educational_dvd.title}")

    def remove(self):
        __dvd_no = input("Enter DVD Number:")
        matched_data = list(x for x in self.list_of_educational_dvds if x.dvd_no == __dvd_no)
        for x in matched_data:
            self.list_of_educational_dvds.remove(x)
            print("Item Removed.")

    def lend(self):
        __dvd_no = input("Enter DVD Number:")
        __copies = int(input("Enter Lend Copies:"))
        matched_data = list(x for x in self.list_of_educational_dvds if x.dvd_no == __dvd_no)
        for x in matched_data:
            x.copies -= __copies
            print("Educational DVD Lent")

    def receive(self):
        __dvd_no = input("Enter DVD Number:")
        __copies = int(input("Enter Receive Copies:"))
        matched_data = list(x for x in self.list_of_educational_dvds if x.dvd_no == __dvd_no)
        for x in matched_data:
            x.copies += __copies
            print(f"Educational DVD Received With {__copies} Copies")

    def display_available(self):
        matched_data = list(x for x in self.list_of_educational_dvds if x.copies > 0)
        for x in matched_data:
            print_info(educational_dvd=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_educational_dvds if x.copies == 0)
        for x in matched_data:
            print_info(educational_dvd=x)


