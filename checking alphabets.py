c = input("Enter a Letter: ")

if c >= "a" and c <= "z":
    print(f"The character {c} is a LOWERCASE Alphabet")
    
elif c >= "A" and c <="Z":
    print(f"The character {c} is a UPPERCASE Alphabet")
    
else:
    print(f"The character {c} is NOT an Alphabet")