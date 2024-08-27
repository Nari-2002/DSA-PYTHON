def countDgts(n):
    c=0
    while n>0:
        c+=1
        n//=10
    return c

n= int(input("Enter a number: "))
print(f"{n} has {countDgts(n)} digits")