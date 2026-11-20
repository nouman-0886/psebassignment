scores = [45, 82, 67, 91, 73]

highest = scores[0]
secHighest = scores[0]

for score in scores:
    if score > highest:
        secHighest = highest
        highest = score

    elif score > secHighest and score < highest:
        secHighest = score

print(highest)
print(secHighest)