students = [("Ali", 85), ("Sara", 92), ("Ahmed", 65), ("Usman", 78)]

# ********Print each student
for name, marks in students:
    print(f"{name} scored {marks}")

# ********Find the topper
topper = students[0]

for student in students:
    if student[1] > topper[1]:
        topper = student

print("Topper:", topper[0], topper[1])

# ************8Find passed students
passed = []

for name, marks in students:
    if marks >= 70:
        passed.append(name)

print("Passed students:", passed)