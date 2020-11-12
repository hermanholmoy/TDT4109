def leap_year(y):
    return True if y % 4 == 0 else False


mnd = input("Skriv inn en måned: ").lower()
år = int(input("Skriv inn et år: "))


if år not in range(0, 2021):
    print("Ugyldig input!")
else:
    if mnd == "januar":
        print(31)
    elif mnd == "februar":
        if leap_year(år):
            print(29)
        else:
            print(28)
    elif mnd == "mars":
        print(31)
    elif mnd == "april":
        print(30)
    elif mnd == "mai":
        print(31)
    elif mnd == "juni":
        print(30)
    elif mnd == "juli":
        print(31)
    elif mnd == "august":
        print(31)
    elif mnd == "september":
        print(30)
    elif mnd == "oktober":
        print(31)
    elif mnd == "november":
        print(30)
    elif mnd == "januar":
        print(31)
    else:
        print("Ugyldig input. ")