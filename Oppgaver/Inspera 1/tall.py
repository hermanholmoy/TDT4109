tall = []

for i in range(5):
    num = float(input("Skriv inn et tall: "))
    tall.append(num)

print(f"Det minste tallet du skrev inn var {min(tall)}")