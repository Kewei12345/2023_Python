array = [6, 2, 4, 8, 1, 4, 7, 1, 9, 12, 4, 9, 0]

def BubbleSort(array):

    Size = len(array)
    index = 0

    for loops in range(Size - 1):
        for index in range(Size - 1 - loops):
            if array[index] > array[index + 1]:
                array[index+1], array[index] = array[index], array[index + 1]

    return array

print(BubbleSort(array))

"""
Array = []

FUNCTION BubbleSort(MyArr) RETURNS ARRAY

    Size = LEN(MyArr)
    Index = 1

    FOR Loops = 1 TO Size - 2
        FOR Index = 1 TO Size - 2 - Loops
            IF MyArr[Index] > MyArr[Index + 1] THEN
                MyArr[index] = Temp
                MyArr[index] = MyArr[index + 1]
                My[Index + 1] = Temp
            ENDIF
        NEXT
    NEXT
    RETURN MyArr
ENDFUNCTION
"""