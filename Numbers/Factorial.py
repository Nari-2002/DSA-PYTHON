def fact(num):
    if num<0:
        return -1
    if num==1 or num==0:
        return 1
    else:
        return num*fact(num-1)
n=int(input("Enter a num: "))
print(f"Factorial of {n} is {fact(n)}")