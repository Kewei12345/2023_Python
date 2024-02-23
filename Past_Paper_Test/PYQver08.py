def IteractiveVowels(Value):
    Total = 0
    LengthString = len(Value)
    for x in range(0, LengthString):
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total += 1  
        Value = Value[1:len(Value)]
    return Total

def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    else:
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            WithoutFirst = Value[1:len(Value)]
            return 1 + RecursiveVowels(WithoutFirst)
        else:
            WithoutFirst = Value[1:len(Value)]
            return RecursiveVowels(WithoutFirst)

print(IteractiveVowels("house"))
print(RecursiveVowels("imagine"))
