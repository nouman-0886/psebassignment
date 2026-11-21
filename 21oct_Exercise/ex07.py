# Exercise 7: Shop discount

price = 3509

if price >= 5000:
    discount = price *(10 / 100)
    print(f"Discount :{discount}, Pay { price - discount}")
elif price > 2000 and price < 5000:
    discount = price *(5 / 100)
    print(f"Discount :{discount}, Pay { price - discount}")
else:
    discount = price *(0 / 100)
    print(f"Discount :{discount}, Pay { price - discount}")
    
    
    
