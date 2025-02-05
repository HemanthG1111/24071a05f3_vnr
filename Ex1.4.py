def add(x,y): #Addition
    return x + y

def subtract(x,y): #Subtraction
    return x - y

def multiply(x,y): #Multiplication
    return x * y

def divide(x,y): #Division
    if y == 0:
        return "Error"
    return x / y

def calculator():
    while True:
        print("Select operation:")
        print("Addition - 1")
        print("Subtraction - 2")
        print("Multiplication - 3")
        print("Division - 4")
        print("Exit - 5")

        op = int(input("Enter operation number: "))
        
        if op == 5:
            return 0

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        
        if op == 1:
            print(f"{x} + {y} = {add(x, y)}")
        elif op == 2:
            print(f"{x} - {y} = {subtract(x, y)}")
        elif op == 3:
            print(f"{x} * {y} = {multiply(x, y)}")
        elif op == 4:
            print(f"{x} / {y} = {divide(x, y)}")
        else:
            print("Invalid, Enter Again")

calculator()