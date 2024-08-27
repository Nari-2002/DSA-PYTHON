num = int(input("Enter a number: "))
binary = bin(num)[2:]
hexa=hex(num)[2:]
octal=oct(num)[2:]
print(f"The binary representation of {num} is {binary}")
print(f"The hexa decimal representation of {num} is {hexa}")
print(f"The octal representation of {num} is {octal}")
