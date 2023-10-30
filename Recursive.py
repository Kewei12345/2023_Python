"""
FUNCTION Factorial(n : INTEGER) RETURNS INTEGER
    IF n = 0 THEN
        Answer = 1
    ELSE
        Answer <- n * Factorial(n-1)
    ENDIF
    RETURN Answer
ENDFUNCTION

PROCEDURE Iterative_Count_Down(n : INTEGER)
    FOR i <- 0 TO n+1
        OUTPUT n-i
    NEXT i
ENDPROCEDURE

PROCEDURE Recursive_Count_Down(n : INTEGER)
    IF n > 0 THEN
        OUTPUT n
        CALL Recursive_Count_Down(n-1)
    ENDIF
ENDPROCEDURE
"""
def Factorial(n):
    if n == 0:
        Answer = 1
    else:
        Answer = n * Factorial(n-1)
    return Answer

def Iterative_Count_Down(n):
    for i in range(0,n):
        print(n-i)

def Recursive_Count_Down(n):
    if n > 0:
        print(n)
        Recursive_Count_Down(n-1)
    
Iterative_Count_Down(5)
Recursive_Count_Down(5)


