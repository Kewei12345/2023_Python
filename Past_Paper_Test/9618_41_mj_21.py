arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def linearSearch(myInt):

    n = 0
    found = False
    while not found:
        if arrayData[n] == myInt:
            found = True
            bool = True
        elif n >= len(arrayData) - 1:
            found = True
            bool = False
        else:
            n += 1

    return bool


#main
user = int(input("Enter a integer: "))
if linearSearch(user):
    print("Search value was found")
else:
    print("Search value not found")
            

def bubbleSort():
    temp = 0
    for x in range (len(arrayData) - 1):
        for y in range(len(arrayData) - 1 - x):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp

bubbleSort()
print(arrayData)