# Q5. Grade report from a dictionary


students = {"Ali": 85, "Sara": 92, "Ahmed": 76, "Hina": 58, "Bilal": 64}

for stu, marks in students.items():
    if marks >= 80:
        print(f"{stu} got {marks} with A")
    elif marks >= 70:
        print(f"{stu} got {marks} with B")
    elif marks >= 60:
        print(f"{stu} got {marks} with C")
    if marks < 60:
        print(f"{stu} got {marks} with F")