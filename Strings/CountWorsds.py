def countlWords(s):
    words=s.split()
    return max(words,key=len)
s=input("enter a string: ")
print(f"largest word is: {countlWords(s)}")