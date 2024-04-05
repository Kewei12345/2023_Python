arr = [12, 3, 54, 32, 56, 99, 69, 87, 431, 2, 33, 67, 59, 71]

size = len(arr) 

for n in range(1, size):

    Item = arr[n]
    SortedIndex = n - 1

    while SortedIndex >= 0 and Item < arr[SortedIndex]:
        arr[SortedIndex + 1] = arr[SortedIndex]
        SortedIndex -= 1
    arr[SortedIndex + 1] = Item

print(arr)