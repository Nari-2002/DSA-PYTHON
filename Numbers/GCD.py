def GCD(a, b):
    while b != 0:  # Continue until the remainder is zero

        a, b = b,a%b
    return a  # When b is 0, a is the GCD

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(f"GCD of {a} and {b} is {GCD(a, b)}")
