# Q1. Pass or fail list


marks = [78, 45, 92, 33, 67, 88]

passed = 0
faild = 0

for mark in marks:
    if mark >= 40:
        print(mark,"Passed")
        passed += 1
    else:
        print(mark,"Failed")
        faild += 1

print(f"Total passed Students '{passed}' out of '{len(marks)}'")
print(f"Total failed Students '{faild}' out of '{len(marks)}'")