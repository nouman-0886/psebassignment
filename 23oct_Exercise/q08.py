# Q8. Unique values and the most frequent


nums = [3, 5, 3, 8, 5, 3, 9]
dec = {}


for num in nums:
    if num in dec:
        dec[num] += 1
    else:
        dec[num] = 1

# print(dec)

print("Unique numbers",list(dec.keys()))
print("Print most frequent num",max(dec, key=dec.get))