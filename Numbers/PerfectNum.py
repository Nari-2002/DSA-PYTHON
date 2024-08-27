def isPerfectNum(n):
    return 'perfect' if sum(i for i in range(1, n) if n % i == 0) == n else 'not perfect'

a = int(input("Enter a number: "))
print(f"{a} is {isPerfectNum(a)} number")
