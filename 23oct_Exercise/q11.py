# Q11. Simple ATM


blance = 10000
history = []


while True:
    print("Deposit amount")
    print("Withdraw amount")
    print("check Blance")
    print("Exit")

    choice = input("Slect option from menu ")

    if choice == "1":
        deposit = int(input("Enter amount: "))

        if deposit > 0:
            blance += deposit

            print(f"{deposit} 3$ is added to you villat")
            history.append(("Deposited", deposit))

            print("Your Updated blance is ",blance,"$")
            print()
        else:
            print("Anount be greater than ",deposit,"$")
    elif choice == "2":
        withdraw = int(input("Enter amount to Withdraw: "))
        print()

        if withdraw > blance:
            print("Insufficient balance")
        else:
            blance -= withdraw

            print("$",withdraw,"has been deducted from your willat")
            print("Your remainig blance is",blance,"$")
            print()

            history.append(("Withdrawn", withdraw))
    elif choice == "3":
        print("You have $",blance,"in your account")

        print()
    elif choice == "4":
        print(history)
        break







           