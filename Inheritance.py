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
        print(self.Title)
        print(self.Author) 
        print(self.ReferenceNum) 
        print(self.Loan)
        print(self.Date)
        try:
            print(self.Requested)
        except AttributeError:
            pass
        try:
            print(self.Genre)
        except AttributeError:
            pass
        print("———————————————————————————————————")


#Child Book of Parent LibraryItem
class Book(LibraryItem):

    def __init__(self, Title, Author, ReferenceNum, Loan):
        super().__init__(Title, Author, ReferenceNum, Loan)
        if Loan:
            self.Requested = True


#Child CD of Parent LibraryItem
class CD(LibraryItem):

    def __init__(self, Title, Author, ReferenceNum, Loan, Genre):
        super().__init__(Title, Author, ReferenceNum, Loan)
        self.Genre = Genre


bookmine = Book("giaw", "seecas", 132, True)
song = CD("hehe", "gaga", 6969, False, "Pop")


bookmine.Output()
song.Output()