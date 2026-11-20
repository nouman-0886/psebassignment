# Print the total, the average, the highest, the lowest, and how many marks are above 70 (use a loop).

marks = [78, 92, 65, 88, 54]
sum = 0
for mark in marks:
    sum += mark

# print(sum)
# print(sum(marks))


# ****** Highest
highest = 78

for mark in marks:
    if mark > highest:
        highest = mark

print(highest)


# ****** LOwest 
lowest = 54

for mark in marks:
    if mark < lowest:
        lowest = mark

print(lowest)

# Above 70

above = []
for mark in marks:
    if mark > 70:
        above.append(mark);
print(len(above))





