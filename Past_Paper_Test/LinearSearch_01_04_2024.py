"""
ARRAY = []
Item = 0

FUNCTION LinearSearch(Arr, Item) RETURNS INTEGER
    DECLARE Index : INTEGER
    DECLARE Found : BOOLEAN
    DECLARE Value : INTEGER

    Index = 1
    Found = FALSE
    Value = -1

    WHILE Found = FALSE DO
        IF Index >= LEN(Arr) THEN
            Found = TRUE
        ELSE
            IF Arr[Index] = Item:
                Found = TRUE
                Value = Index
            ELSE
                Index = Index + 1
            ENDIF
        ENDIF
    ENDWHILE
    RETURN Value
ENDFUNCTION
"""

array = [1, 3, 6, 8, 9]
item = 10

def linSear(arr, item):
    n = 0
    Found = False
    Value = -1

    while not Found:
        if n >= len(arr):
            Found = True
        elif arr[n] == item:
            Found = True
            Value = n
        else:
            n += 1
    return Value

print(linSear(array, item))

