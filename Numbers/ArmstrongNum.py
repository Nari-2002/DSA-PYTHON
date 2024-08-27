def isArmstrng(n):
    t=n
    sum=0
    while n>0:
        r=n%10
        sum=sum+r**3
        n//=10
    return "Armstrong" if(sum==t) else "Not Armstrong"


a = int(input("Enter a number: "))
print(f"{a} is {isArmstrng(a)} number")