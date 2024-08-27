import math
def LCM(a,b):
    return abs(a*b)//math.gcd(a,b)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(f"LCM of {a} and {b} is {LCM(a, b)}")
