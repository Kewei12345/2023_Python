global Head
global Tail
global NumItems
global Queue


Head = 0
Tail = 0
NumItems = 0
Queue = [0 for i in range(10)]


def Enqueue(InputData):
    global Head
    global Tail
    global NumItems
    global Queue

    if NumItems >= 10:
        return False
    Queue[Tail] = InputData
    if Tail >= 9:
        Tail = 0
    else:
        Tail += 1
    NumItems += 1
    return True


def Dequeue():
    global Head
    global Tail
    global NumItems
    global Queue

    if NumItems == 0:
        return False
    else:   
        ReturnValue = Queue[Head]
        Head += 1
        if Head >= 9:
            Head = 0
        NumItems -= 1
        return ReturnValue
    
#main
for n in range(11):
    User = input("11 strings: ")
    if Enqueue(User): 
        print("Successful")
    else:
        print("Unsuccessful")

print(Dequeue())
print(Dequeue())
