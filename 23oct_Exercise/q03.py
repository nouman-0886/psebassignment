# Highest and lowest price



prices = [450, 1200, 300, 980, 75]

highest = 0
lowest = 75

for price in prices:
    if price >= highest:
        highest = price
    if price <= lowest:
        lowest = price


print(f"Highest price {highest}")
print(f"Lowest price {lowest}")