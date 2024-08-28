from collections import Counter
def displayFrequency(s):
    return Counter(s)
s=input("enter a string: ")
print(f"frequency of chars : {displayFrequency(s)}")
