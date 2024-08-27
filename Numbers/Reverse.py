def rev(n):
    r=0
    while n>0:
        d=n%10
        r=r*10+d
        n//=10
    return r
def revs(n):
    return int(str(n)[::-1])
n=int(input("Enter a num: "))
print(f"reverse of {n} is {rev(n)}")
print(f"reverse of {n} is {revs(n)}")