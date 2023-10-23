"""
FUNCTION BubbleSort(MyList : ARRAY) RETURNS ARRAY
    DECLARE Count, Current, Temp : INTEGER

 

    FOR Count <- 1 TO LEN(MyList)
        FOR Index <- 1 TO LEN(MyList) - Count
            IF MyList[Index] > MyList[Index + 1] THEN
                Temp = MyList[Index]
                MyList[Index]  = MyList[Index + 1]
                MyList[Index + 1] = Temp
        NEXT Index
    NEXT Count
    RETURNS MyList
ENDFUNCTION
"""

 
def BubbleSort(MyList):
    Temp = 0;
    for Count in range(0, len(MyList)-1):
        for Index in range(len(MyList)-1-Count):
            if MyList[Index] > MyList[Index + 1]:
                MyList[Index], MyList[Index + 1] = MyList[Index + 1], MyList[Index]
    return MyList
   
List = [10, 4, 7, 2, 3, 8, 1, 9, 5, 6]
print(BubbleSort(List))
