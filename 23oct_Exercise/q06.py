# Q6. Even and odd counter




numbers = [12, 7, 9, 20, 33, 48, 51]
result = {"even": 0, "odd": 0}

for num in numbers:
    if num % 2 == 0:
     result["even"] += 1
    else:
     result["odd"] += 1
        


print(result)
