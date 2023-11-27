from classes import Lecture_CD

def print_info(lecture_cd):
    print(f"CD NO: {lecture_cd.cd_no}, Title: {lecture_cd.title}, Subject: {lecture_cd.subject}, Rental Price: {lecture_cd.rental_price}, Available Copies:{lecture_cd.copies}")

class Lecture_CD_Function:

    def __init__(self):
        self.list_of_lecture_cd = []
        self.__initial_data()

    def __initial_data(self):
        a_lecture_cd1 = Lecture_CD(cd_no="21", title="Basics of Western Music,", subject="Music", rental_price=120.50, copies=5)
        a_lecture_cd2 = Lecture_CD(cd_no="22", title="A Mathematician's Lament", subject="Math", rental_price=100.50, copies=0)
        a_lecture_cd3 = Lecture_CD(cd_no="23", title="One Hundred Years of Solitude", subject="Foreign Languages", rental_price=500.50, copies=10)
        self.list_of_lecture_cd.append(a_lecture_cd1)
        self.list_of_lecture_cd.append(a_lecture_cd2)
        self.list_of_lecture_cd.append(a_lecture_cd3)

        print(self.list_of_lecture_cd[0].cd_no)

    def add(self):
        __cd = input("Enter CD Number:").strip().upper()

        for educational_dvd in self.list_of_lecture_cd:
            if __cd == educational_dvd.cd_no:
                print(f"{__cd} This dvd number is already in this system")
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

        a_lecture_cd = Lecture_CD(cd_no=__cd, title=__title, subject=__subject, rental_price=__rental_price, copies=__copies)
        self.list_of_lecture_cd.append(a_lecture_cd)
        print(f"Book Added {a_lecture_cd.cd_no}-{a_lecture_cd.title}")

    def remove(self):
        __cd = input("Enter CD number:")
        matched_data = list(x for x in self.list_of_lecture_cd if x.cd_no == __cd)
        for x in matched_data:
            self.list_of_lecture_cd.remove(x)
            print("Item Removed.")

    def lend(self):
        __cd = input("Enter CD number:")
        __copies = int(input("Enter Lend Copies:"))
        matched_data = list(x for x in self.list_of_lecture_cd if x.cd_no == __cd)
        for x in matched_data:
            x.copies -= __copies
            print("Lecture CD Lent")

    def receive(self):
        __cd = input("Enter ISBN number:")
        __copies = int(input("Enter Receive Copies:"))
        matched_data = list(x for x in self.list_of_lecture_cd if x.cd_no == __cd)
        for x in matched_data:
            x.copies += __copies
            print(f"Lecture_CD Received with {__copies} Copies")

    def display_available(self):
        matched_data = list(x for x in self.list_of_lecture_cd if x.copies > 0)
        for x in matched_data:
            print_info(lecture_cd=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_lecture_cd if x.copies == 0)
        for x in matched_data:
            print_info(lecture_cd=x)


