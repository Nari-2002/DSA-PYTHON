def evenOrOdd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
n=int(input("Enter a num: "))
print(f"{n} is {evenOrOdd(n)}")
