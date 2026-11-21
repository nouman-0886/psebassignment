# Exercise 9: Triangle checker

a = 5
b = 4
c = 8

if (a + b > c) and (a + c > b) and (b + c > a):
    print(f"Sides {a}, {b}, and {c} form a Valid Triangle.")
    if a != b and b != c and c != a:
         print(f"Valid Scalene Triangle with lengths {a}, {b}, {c}")
    elif a == b or b == c or a == c:
        print(f"Valid Isosceles Triangle with lengths {a}, {b}, {c}")
else:
    print("Invalid Triangle.")