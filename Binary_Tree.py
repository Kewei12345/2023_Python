"""
CONSTANT NullPtr <- -1

TYPE TreeNode
    DECLARE Data : STRING
    DECLARE LeftPtr : INTEGER 
    DECLARE RightPtr : INTEGER
ENDTYPE

DECLARE RootPtr : INTEGER
DECLARE FreePtr : INTEGER
DECLARE Tree : ARRAY[0:MaxNodes] Of TreeNode

PROCEDURE InitTree
    RootPtr <- NullPtr
    FreePtr <- 0
    FOR i <- 0 TO 5
        Tree[i].LeftPtr <- i + 1
    NEXT InitTree
    
    Tree[6].LeftPtr <- NullPtr
ENDPROCEDURE
""" 

#Creating

NullPtr = -1 #CONSTANT

class TreeNode:
    def __init__(self, Data=None, LeftPtr=NullPtr, RightPtr=NullPtr):
        self.Data = Data
        self.LeftPtr = LeftPtr
        self.RightPtr = RightPtr

RootPtr = 0
FreePtr = 0
Tree = [TreeNode() for _ in range(7)]

def InitTree():
    RootPtr = NullPtr
    FreePtr = 0
    for i in range(6):
        Tree[i].LeftPtr = i + 1

    Tree[6].LeftPtr = NullPtr
        
#Insert

def Insert(NewItem):
    global RootPtr, FreePtr
    if FreePtr != NullPtr:
        NewNodePtr = FreePtr
        FreePtr = Tree[FreePtr].LeftPtr
        Tree[NewNodePtr].Data = NewItem
        Tree[NewNodePtr].LeftPtr = NullPtr
        Tree[NewNodePtr].RightPtr = NullPtr
        if RootPtr == NullPtr:
            RootPtr = NewNodePtr
        else:
            ThisNodePtr = RootPtr
            while ThisNodePtr != NullPtr:
                PreviousNodePtr = ThisNodePtr
                if NewItem == Tree[ThisNodePtr].Data:
                    TurnedLeft = True
                    ThisNodePtr = Tree[ThisNodePtr].LeftPtr
                else:
                    TurnedLeft = False
                    ThisNodePtr = Tree[ThisNodePtr].RightPtr
            if TurnedLeft:
                Tree[PreviousNodePtr].LeftPtr = NewNodePtr
            else:
                Tree[PreviousNodePtr].RightPtr = NewNodePtr

#Find

def Find(SearchItem):
    ThisNodePtr = RootPtr
    while ThisNodePtr != NullPtr and Tree[ThisNodePtr].Data > SearchItem:
        if SearchItem < Tree[ThisNodePtr].Data:
            ThisNodePtr = Tree[ThisNodePtr].LeftPtr
        else:
            ThisNodePtr = Tree[ThisNodePtr].RightPtr
    return ThisNodePtr
