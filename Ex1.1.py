def Check_Prime(n):
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

n = int(input("Enter Number: "))

if Check_Prime(n):
    print("Given number is a Prime number")
else:
    print("Given number is not a Prime number")