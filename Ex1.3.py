def lcm(a, b):
    i = max(a, b)
    while True:
        if i%a == 0 and i%b == 0:
            return i
        i += 1

def gcd(a, b):
    return (a * b) // lcm(a, b)    # // for returning integers like 6 instead of float point value like 6.0

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

r_lcm = lcm(a,b)
r_gcd = gcd(a,b)

print(f"The LCM is: {r_lcm}")
print(f"The GCD is: {r_gcd}")
