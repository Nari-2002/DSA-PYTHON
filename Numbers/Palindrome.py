def palin(n):
    num=n
    r=0
    while n>0:
        d=n%10
        r=r*10+d
        n//=10
    return "palindrome" if num==r else "not palindrme"
def palindrome(n):
    return "palindrome" if int(str(n)[::-1])==n else "not palindrme"
n=int(input("Enter a num: "))
print(f"{n} is {palin(n)}")
print(f"{n} is {palindrome(n)}")