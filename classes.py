# --------------Book------------------
class Book:
    def __init__(self, isbn_no, title, format, subject, rental_price, copies):
        self.isbn_no = isbn_no
        self.title = title
        self.format = format
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies


# --------------Magazine------------------
class Magazine:
    def __init__(self, m_no, title, color, subject, rental_price, copies):
        self.m_no = m_no
        self.title = title
        self.color = color
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies


# --------------Educational_DVD------------------
class Educational_DVD:
    def __init__(self, dvd_no, title, subject, rental_price, copies):
        self.dvd_no = dvd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies


# --------------Lecture_CD------------------
class Lecture_CD:
    def __init__(self, cd_no, title, subject, rental_price, copies):
        self.cd_no = cd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies
