def Unknown(x, y):
    if x < y:
        print(x + y)
        return Unknown(x + 1, y) * 2
    
    elif x == y:
        return 1
        
    else:
        print(x + y)
        return Unknown(x - 1, y) // 2
    

def IterativeUnknown(x, y):
    Power = 1
    while x != y:
        print(x + y)
        if x < y:
            Power *= 2
            x += 1

        else:
            Power //= 2
            x -= 1

    return Power
    
print("Two parameters are: [10] and [15]")
print(Unknown(10, 15))
print("Two parameters are: [10] and [10]")
print(Unknown(10, 10))
print("Two parameters are: [15] and [10]")
print(Unknown(15, 10))
print("______________________________________________")
print("Two parameters are: [10] and [15]")
print(IterativeUnknown(10, 15))
print("Two parameters are: [10] and [10]")
print(IterativeUnknown(10, 10))
print("Two parameters are: [15] and [10]")
print(IterativeUnknown(15, 10))