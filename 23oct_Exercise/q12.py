# Q12. Password checker (bonus)





while True:
    password = input("Enter password: ")

    has_digit = False
    has_upper = False
    is_long = False

    if len(password) >= 8:
        is_long = True
    else:
        print("Password Must has more than 8 char")
        print()

    for char in password:

        if char.isdigit():

            has_digit = True

        if char.isupper():

            has_upper = True
        


    if has_upper == True and has_digit == True and is_long:

        print(password," Password accepted")

        print()
        break
    else:
        print(password," Weak password")

        print()
    # has_digit = False
    # has_upper = False
    # is_long = False



print(password)
    




