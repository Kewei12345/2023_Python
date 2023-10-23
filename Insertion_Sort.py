"""
PROCEDURE InsertionSort(a : ARRAY)
    FOR i <- 2 TO LEN(a)
       
        temp <- a[i]
       
        j <- i-1
        WHILE j >= 1 AND temp < a[j] DO
                a[j+1] <- a[j]
                j <- j - 1
        ENDWHILE
        a[j+1] <- temp
    NEXT i
ENDPROCEDURE
"""
def InsertionSort(a):
  
    for i in range(1, len(a)):
  
        temp = a[i]
  
        j = i-1
        while j >=0 and temp < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp

 

 

MyList = [54, 17 ,34, 15, 84, 37, 61, 27, 8]
InsertionSort(MyList)
print(MyList)

#Messy version

array = [7, 9, 75, 56, 12, 99, 37, 48, 87, 26, 69]
sortedArray = [array[0]]
unsortedArray = array.copy()
unsortedArray.pop(0)

 

for unsortedPos in range(0, len(array) -1):
    item = unsortedArray[unsortedPos]
    sortedPos = unsortedPos
    posFound = False
    while not posFound:
        if sortedArray[sortedPos] > item:
            sortedPos -= 1
        else:
            posFound = True
        if sortedPos == -1:
            posFound = True
    
    sortedArray.insert(sortedPos +1, item)
print(sortedArray)
