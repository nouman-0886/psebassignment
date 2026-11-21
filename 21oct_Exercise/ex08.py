# Exercise 8: Character type


char = input("Enter you Charcter")

if char.lower() in "aeiou" and len(char) == 1:
    print(f"'{char}' is Vowel")
elif char.isdigit() and len(char) == 1:
    print(f"'{char}' is Digit")
elif char.isalpha() and len(char) == 1:
    print(f"'{char}' is Constant")
elif len(char) == 1:
    print(f"'{char}' is a Special Character")
else:
    print(f"'{char}' is not Valid in Givin Condition")
    