def countVC(s):
    vowels='aeiouAEIOU'
    vc=sum(1 for i in s if i in vowels)
    cc=sum(1 for i in s if i not in vowels)
    return [vc,cc]
s=input("enter a string: ")
count=countVC(s)
print(f"vowels : {count[0]}\nconsonents : {count[1]}")
