#Queues

EMPTYSTRING = "" #CONSTANT
NullPointer = -1 #CONSTANT
MaxQueueSize = 8 #CONSTANT

FrontOfQueuePointer = 0
EndOfQueuePointer = 0
NumberInQueue = 0

Queue = ["" for _ in range(MaxQueueSize)]

def InitialiseQueue():
    global FrontOfQueuePointer, EndOfQueuePointer, NumberInQueue
    FrontOfQueuePointer = NullPointer
    EndOfQueuePointer = NullPointer
    NumberInQueue = 0

#Add

def Enqueue(NewItem):
    global EndOfQueuePointer, NumberInQueue
    if NumberInQueue < MaxQueueSize:
        EndOfQueuePointer += 1
        if EndOfQueuePointer > MaxQueueSize - 1:
            EndOfQueuePointer = 0;
        Queue[EndOfQueuePointer] = NewItem
        NumberInQueue += 1
