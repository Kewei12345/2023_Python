def main():
    def binarySearch(array, x):
        low = 0
        high = len(array) - 1
        found = False
        out = 0
            
        if x < array[low] or x > array[high]:
            out = -1
            found = True
        while not found:
            mid = (high + low)//2
            if array[mid] == x:
                out = mid
                found = True
            elif array[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
                    
        return out
            
    def userInput():
        
        highNum = int(input("high: "))
        lowNum = int(input("low: "))
        array = []
        
        for count in range(highNum - lowNum + 1):
            array.append(lowNum + count)
            
        return array
    
    array = userInput()
    print(f"Your array: {array}")
    searchFor = int(input("search value: "))
    print(binarySearch(array, searchFor))
    
main()
