#DECLARE TheData : ARRAY[9] LOCAL
TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]


def InsertionSort(MyData):
    for Count in range(0, len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue -= 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1


def Output(MyDataAgain):
    for n in range(len(MyDataAgain)):
        print(MyDataAgain[n], end = " ")


def NumInputCheck(TheData):
    User = int(input("Whole Number: "))
    if User in TheData:
        print("Found")
        return True
    else:
        print("No Found")
        return False



#main
print("__Before__")
Output(f"{TheData}\n")
print("__After__")
InsertionSort(TheData)
Output(f"{TheData}\n")


NumInputCheck(TheData)
NumInputCheck(TheData)