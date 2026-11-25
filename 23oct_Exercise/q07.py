# Q7. Stock check with tuples

products = [("Laptop", 150000, 3), ("Mouse", 2500, 0),
("Keyboard", 5000, 12), ("Monitor", 45000, 2)]


for prod in products:
    if prod[2] == 0:
        print(f"Currently '{prod[0]}' is out of Stock")
    if prod[2] >= 1 and prod[2] <= 4:
        print(f"Currently '{prod[0]}' is in low Stock")
    
print(f"Total paybale : {prod[1] * prod[2]} ")
