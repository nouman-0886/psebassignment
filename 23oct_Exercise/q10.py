# Q10. Shopping cart menu

cart = {}


while True:
    print("Add item")
    print("View cart")
    print("Chackout")

    choice = input("Enter you choice " )
       
    if choice == "1":
        item = input("Enter Item: ")
        price = int(input("Enter price: "))

        cart[item] = price
        print(f"{item} added Sucessfully")
    elif choice == "2":
        total = sum(cart.values())

        for prod, keemt in cart.items():

            print(f"{prod} has price of Rs {keemt}")

        print("Total", total)
    elif choice == "3":
        total = sum(cart.values())

        if total > 5000:
            discount = total * 0.10
            final_price = total - discount

            print("Diccounted prdice",discount)
            print("Total price:", final_price)
        else:
            print("Total price:", total)

        break
    else:
        print("Invalid Request")
            
