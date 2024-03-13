## 1. Implement python program for recursion

## a.
def recursionA(n: int) -> int:
    match n:
        case 0:
            return 0
        case _:
            return 2-(n-1)

## b.
def f(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    value = f(n-1) - f(n-2)
    return value
        
## c.
def recursionC(n: int) -> int:
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 1
        case _:
            return (n-1)-(n-2)+(2*(n-3))

## Python and logic

def ifthen(x,y): # no builtin if..then. Build
    return (not x) or y 

## 1. 
def pythonA(x, y, z: bool) -> bool:
    logicValue = (not x or y) and z
    return logicValue

## 2. 
def f( x,y: bool) -> bool:
    return (not x or y)

def classify(f: callable[[bool, bool], bool]) -> None:

    # Create flags
    tautology = True
    contradiction = True

    # Loop through all possible values of x and y
    for x in {True, False}:
        for y in {True, False}:
            if (f(x,y)):
                contradiction = False
            else:
                tautology = False
    if contradiction:
        print("This function is a contradiction")
    elif tautology:
        print("This function is a tautology")
    else:
        print("This function is a contingent")
        print("The function is satisfiable")

    return None

# 3. Write a function which takes two formulas and finds if they are logically equivalent or not

def testLE(f: callable[[bool, bool], bool], g: callable[[bool, bool], bool]) -> None:
    for x in {True, False}:
        for y in {True, False}:
            if (f(x,y) != g(x,y)):
                print("The functions are not logically equivalent")
                return None
    print("The functions are logically equivalent")
    return None