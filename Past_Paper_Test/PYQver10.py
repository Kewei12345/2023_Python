def IterativeCalculate(Num):
    #Total : INTEGER
    #ToFind : INTEGER
    ToFind = Num
    Total = 0
    while Num != 0:
        if ToFind % Num == 0:
            Total += Num
        Num -= 1
    return Total

print(IterativeCalculate(10))

    
def RecursiveValue(Number, ToFind):
    if Number == 0:
        return 0
    elif ToFind % Number == 0:
         return Number + RecursiveValue(Number - 1, ToFind)
    else:
        return RecursiveValue(Number - 1, ToFind)
    
print(RecursiveValue(50, 50))