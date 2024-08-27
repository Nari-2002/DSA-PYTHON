# using recursive method
def sumOfDgts(n):
    sum=0
    while n>0:
        d=n%10
        sum=sum+d
        n//=10
    return sum

# using list Comprehension
def sumdgts(n):
    return sum(int(digit) for digit in str(n))
n=int(input("Enter a num: "))
print(f"sum of digits in {n} is {sumOfDgts(n)}")
print(f"sum of digits in {n} is {sumdgts(n)}")

