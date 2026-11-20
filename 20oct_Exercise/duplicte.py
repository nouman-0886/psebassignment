# ****** DUplicate


nums = [3, 1, 3, 2, 1, 5]


unique = []
for num in nums:
    if num not in unique:
        unique.append(num)

print(unique);