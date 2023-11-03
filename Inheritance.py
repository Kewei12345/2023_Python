import datetime

#Parent
class LibraryItem:

    def __init__(self, Title, Author, ReferenceNum, Loan,):
        self.Title = Title
        self.Author = Author 
        self.ReferenceNum = ReferenceNum 
        self.Loan = Loan 
        self.Date = datetime.timedelta(weeks=3)

    def Output(self):
        print("———————————————————————————————————")
        print(f"Title: {self.Title}")
        print(f"Author: {self.Author}") 
        print(f"Reference Number: {self.ReferenceNum}") 
        print(f"Load: {self.Loan}")
        print(f"Date: {self.Date}")

#Child Book of Parent LibraryItem
class Book(LibraryItem):

    def __init__(self, Title, Author, ReferenceNum, Loan):
        super().__init__(Title, Author, ReferenceNum, Loan)
        if Loan:
            self.Requested = True

    def Output(self):
        super().Output()

        print(f"Requested: {self.Requested}")



#Child CD of Parent LibraryItem
class CD(LibraryItem):

    def __init__(self, Title, Author, ReferenceNum, Loan, Genre):
        super().__init__(Title, Author, ReferenceNum, Loan)
        self.Genre = Genre

    def Output(self):
        super().Output()

        print(f"Genre: {self.Genre}")
    


MyBook = Book("BookNameHere", "AuthorNameHere", 132, True)
MyCD = CD("RandomCD", "KeweiChen", 6969, False, "Pop")


MyBook.Output()
MyCD.Output()