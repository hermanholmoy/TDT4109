def data():
    lengde = float(input("Lengde: "))
    bredde = float(input("Bredde: "))
    høyde = float(input("Høyde: "))
    return lengde, bredde, høyde


l, b, h = data()

while True:

    if l != b and b != h and l != h:
        # ulike
        d = min([l, b, h])
        volum = d ** 3
        print(f"Den største kuben blir {round(volum, 2)} m^3")
        break

    else:
        print("Morten er ikke fornøyd, hullet kan ikke graves. Prøv igjen.")
        l, b, h = data()