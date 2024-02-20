QueueData = [""]*20
StartP = 0
EndP = 0


def Enqueue(DTA, QueueData, EndP):
    
    if EndP == 20:
        return False, EndP
    else:
        QueueData[EndP] = DTA
        return True, EndP + 1
    

def ReadFile(QueueData, EndP):
    FName = input("File Name: ")
    Flag = True
    try:
        File = open(FName, "r") 
        Data = File.readline().strip()
        while Flag is True and Data != "":
            Flag, EndP = Enqueue(Data, QueueData, EndP)
            Data = File.readline().strip()
        if Flag is False:
            File.close()
            return 1, EndP
        else:
            File.close()
            return 2, EndP
    except FileNotFoundError:
        return -1, EndP
    

def Remove(QueueData, StartP, EndP):
    if EndP - StartP < 2:
        return "Not enough Items", StartP, EndP
    else:
        Data1 = QueueData[StartP]
        Data2 = QueueData[StartP + 1]
        return Data1 + " " + Data2, StartP + 2, EndP



#main   
BoolValue, EndP = ReadFile(QueueData, EndP)
if BoolValue == -1:
    print("File not found")
elif BoolValue == 1:
    print("Queue is full")
else:
    print("All items added")
