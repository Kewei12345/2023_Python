class TreasureChest:

    def __init__(self, question, answer, points):
        self.__question = question #string
        self.__answer = answer #integer
        self.__points = points #integer

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, UserAns):
        if UserAns == int(self.__answer):
            return True
        else:
            return False
        
    def getPoints(self, Attempts):
        if Attempts == 1:
            return int(self.__points)
        elif Attempts == 2:
            return int(self.__points) // 2
        elif Attempts == 3 or Attempts == 4:
            return int(self.__points) // 4
        else:
            return 0

#arrayTreasure[0:4] as TreasureChest
arrayTreasure = []
def readData():
    global arrayTreasure
    try:
        with open("TreasureChestData.txt", "r") as f:
            ThisLine = f.readline().strip()
            while ThisLine != "":
                Q = ThisLine
                A = f.readline().strip()
                P = f.readline().strip()
                arrayTreasure.append(TreasureChest(Q, A, P))
                ThisLine = f.readline().strip()
    except IOError:
        print("File not found") 
    



#main
readData()
QNum = int(input("Number between 1 and 5: "))
print(arrayTreasure[QNum - 1].getQuestion())
Correct = False
Attempt = 0
while not Correct:
    UserAns = int(input("Your answer: "))
    Correct = arrayTreasure[QNum - 1].checkAnswer(UserAns)
    Attempt += 1
print(f"Points awarded: {arrayTreasure[QNum - 1].getPoints(Attempt)}")

