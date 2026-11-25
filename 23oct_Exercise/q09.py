# Q9. Student report card


students = [
{"name": "Ali", "marks": [80, 75, 90]},
{"name": "Sara", "marks": [95, 88, 92]},
{"name": "Ahmed", "marks": [55, 62, 48]},
]

topper = 0
topper_name = ""



for stu in students:
    mark = stu["marks"]
    average = ((sum(mark) / len(mark)))
    print(f"{average:.2f} is over all average of '{stu["name"]}'")
    if average > 60:
        print(f"{stu['name']} passed with averag of '{average:.2f}'")
        print()
    else:
        print(f"{stu['name']} failed with averag of '{average:.2f}'")
        print()
    if average > topper:
        topper = average
        topper_name = stu["name"]
print(f"{topper_name} is topper in class with average of '{topper:.2f}' ")

        
