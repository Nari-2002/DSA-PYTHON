def palindromeCheck(s):
    return "a palindrome" if(s==s[::-1]) else "Not a palindrome"
s=input("enter a string: ")
print(f"{s} is {palindromeCheck(s)}")