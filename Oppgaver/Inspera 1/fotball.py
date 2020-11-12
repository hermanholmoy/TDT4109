resultater = {
    "h": "Yay, det ble hjemmeseier!",
    "b": "Oufh, så trist å tape på egen bane.",
    "u": "Snufs, men kunne vært verre.",
}

res = input("Hva ble resultatet? ").lower()

if res in resultater.keys():
    print(resultater[res])
else:
    print("Gikk det såpass dårlig ja? Ønsker ikke å snakke om det engang...")