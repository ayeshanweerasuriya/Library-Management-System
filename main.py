from bookfunction import Book_Function
from magazinefunction import Magazine_Function
from educationaldvdfunction import Educational_DVD_Function
from lecturecdfunction import Lecture_CD_Function

book_func = Book_Function()
magazine_func = Magazine_Function()
educational_dvd_func = Educational_DVD_Function()
lecture_cd_func = Lecture_CD_Function()


def mainmenu():
    print("WELCOME TO OUSL LIBRARY MANAGEMENT SYSTEM")
    print("==============================")
    print("Main Menu")
    print("-------------")
    print("1 - Books")
    print("2 - Magazines")
    print("3 - Educational DVDs")
    print("4 - Lecture CDs")
    print("0 - Quit")

    selected_resource = None
    selected_operation = int(input("Please Type The Number Of Your Choice: ").strip())

    if selected_operation == 1:
        selected_resource = "Book"
        submenu(book_func, selected_resource)
    elif selected_operation == 2:
        selected_resource = "Magazine"
        submenu(magazine_func, selected_resource)
    elif selected_operation == 3:
        selected_resource = "Educational_DVD"
        submenu(educational_dvd_func, selected_resource)
    elif selected_operation == 4:
        selected_resource = "Lecture_CD"
        submenu(lecture_cd_func, selected_resource)
    elif selected_operation == 0:
        print("Exiting program...")
    else:
        print("Invalid Selection")


def submenu(resource_func, selected_resource):
    selected_operation = 1
    while selected_operation > 0:
        print(f"{selected_resource} Menu")
        print("--------------------------------")
        print(f"1 - Add a {selected_resource}")
        print(f"2 - Remove a {selected_resource}")
        print(f"3 - Display Available {selected_resource}")
        print(f"4 - Display Unavailable {selected_resource}")
        print(f"5 - Lend {selected_resource}")
        print(f"6 - Receive {selected_resource}")
        print("7 - Back to Main Menu")
        print("0 - Quit")
        selected_operation = int(input("Please Type The Number Of Your Choice: ").strip())

        if selected_operation == 1:
            resource_func.add()
        elif selected_operation == 2:
            resource_func.remove()
        elif selected_operation == 3:
            resource_func.display_available()
        elif selected_operation == 4:
            resource_func.display_unavailable()
        elif selected_operation == 5:
            resource_func.lend()
        elif selected_operation == 6:
            resource_func.receive()
        elif selected_operation == 7:
            mainmenu()
        elif selected_operation == 0:
            print("Exiting program...")
            break
        else:
            print("Invalid Selection")

        if 1 <= selected_operation <= 7:
            input("Press Any Key To Continue...")


if __name__ == '__main__':
    mainmenu()
