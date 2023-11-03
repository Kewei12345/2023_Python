import datetime

class LibraryItems:

    def __init__(self, Title="", AuthorArtist="", ItemID="", OnLoan=False,Date=datetime.date.today()):
        self.__Title = Title
        self.__AuthorArtist = AuthorArtist
        self.__ItemID = ItemID
        self.__OnLoan = OnLoan
        self.__Date = Date

    #Define getters and setters
    def GetTitle(self):
        return self.__Title
    
    def GetAuthorArtist(self):
        return self.__AuthorArtist
    
    def GetItemID(self):
        return self.__ItemID
    
    def GetOnLoan(self):
        return self.__OnLoan
    
    def GetDate(self):
        return self.__Date
    
    def Borrowing(self):
        self.__OnLoan = True
        self.__Date = self.__Date + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False
        self.__Date = datetime.date.today()

    def PrintDetail(self):
        print("———————————————————————————————————")
        print(self.__Title)
        print(self.__AuthorArtist)
        print(self.__ItemID)
        print(self.__OnLoan)
        print(self.__Date)
        print("———————————————————————————————————")





favourite_book = LibraryItems("Stupid", "Kewei", "12345")

favourite_book.PrintDetail()