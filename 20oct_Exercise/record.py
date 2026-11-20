student = ("BSIT-12", "Sara", 88)

section, stuName, rollNo = student

# print(stuName,"studies in" ,section,"her roll number is",rollNo)

# student[2] = 95  #TypeError: 'tuple' object does not support item assignment

# student = ("BSIT-12", "Sara", 88)

string = str(student)

new_string = string.replace("88", "95")

student = eval(new_string)

print(student)
print(type(student))
