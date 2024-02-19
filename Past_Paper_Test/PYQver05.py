#Queue : array[0:49] of string
#HeadP : integer
#TailP : integer

global Queue
global HeadP
global TailP

Queue = []
HeadP = -1
TailP = 0


def Enqueue(DTA):

    global Queue
    global HeadP
    global TailP

    if TailP == 50:
        print("Queue full")
    else:
        Queue.append(DTA)
        TailP += 1
        if HeadP == -1:
            HeadP = 0
    

def Dequeue(DTA):
    
    global Queue
    global HeadP
    global TailP

    if HeadP == -1 or HeadP == TailP:
        print("Queue empty")
        return "Empty"
    else:
        HeadP += 1
        return Queue[HeadP - 1]
    

def readData():

    global Queue
    global HeadP
    global TailP
    try:
        with open("QueueData.txt", "r") as f:
            ThisLine = f.readline().strip()
            while ThisLine != "":
                Enqueue(ThisLine)
                ThisLine = f.readline().strip()
    except IOError:
        print("File not found")


class RecordData:

    def __init__(self, ID, Total;):
        self.ID = ID #string
        self.Total = Total #integer

    def SetID(self, IDP):
        self.ID = IDP

    def GetID(self):
        return self.ID

    def SetTotal(self, TotalP):
        self.Total = TotalP

    def GetTotal(self): 
        return self.Total


#Records : [0:49] of RecordData
#NumberRecords : integer

global Records
global NumberRecords

Records = []
NumberRecords = 0

def TotalData():
    global Records
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False

    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed