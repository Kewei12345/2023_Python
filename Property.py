import datetime

class LibraryItems:

    def __init__(self, Title="", AuthorArtist="", ItemID="", OnLoan=False,Date=datetime.date.today()):
        self.__Title = Title
        self.__AuthorArtist = AuthorArtist
        self.__ItemID = ItemID
        self.__OnLoan = OnLoan
        self.__Date = Date

    #Define getters and setters
    @property
    def GetTitle(self):
        return self.__Title
    
    @property
    def GetAuthorArtist(self):
        return self.__AuthorArtist
    
    @property
    def GetItemID(self):
        return self.__ItemID
    
    @property
    def GetOnLoan(self):
        return self.__OnLoan
    
    @property
    def GetDate(self):
        return self.__Date
    
    def Borrowing(self):
        self.__OnLoan = True
        self.__Date = self.__Date + datetime.timedelta(weeks=3)
    
    def Returning(self):
        self.__OnLoan = False
        self.__Date = datetime.date.today()

    @property
    def PrintDetail(self):
        print("———————————————————————————————————")
        print(self.__Title)
        print(self.__AuthorArtist)
        print(self.__ItemID)
        print(self.__OnLoan)
        print(self.__Date)
        print("———————————————————————————————————")


favourite_book = LibraryItems("Stupid", "Kewei", "12345")


print(favourite_book.GetTitle)
print(favourite_book.GetAuthorArtist)
print(favourite_book.GetItemID)
print(favourite_book.GetOnLoan)
print(favourite_book.GetDate)
