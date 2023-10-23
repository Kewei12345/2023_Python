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
InitTree()
for i in range(7):
    print(f'{Tree[i].Data}, {Tree[i].LeftPtr}, {Tree[i].RightPtr}')
        
