a = [1, 2, 3]

b= a
c= a.copy()

a.append("4")

print(a)
print(b)
print(c)

# copy() method creates a shallow copy of a with same element and is stored in c.SO adding elemnt orignale array does not change its copy

