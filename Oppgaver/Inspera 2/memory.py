def smallify_words(objects):
    return [item.lower() for item in objects]


l = ["Dog", "CATS", "MoUsE"]


def get_five_words():
    print("Input five words separated with ;.")
    words = input().split(";")
    while len(words) != 5:
        print(f"Input five words, not {len(words)}.")
        words = input().split(";")
    
    return smallify_words(words)


def play_game():
    words = get_five_words()
    correct = 0
    guessed = []

    print("Huskelek: ")
    print("Skriv quit for å avslutte.")
    guess = input("Gjett: ")
    while correct != len(words) and guess != "quit":
        if guess in words:
            print(f"Riktig! {guess} er i lista.")
            if guess not in guessed:
                correct += 1
                guessed.append(guess)
        else:
            print("Ikke riktig. Prøv igjen. ")

        if correct == len(words):
            print("Du gjettet alt! Gratulerer.")
        else:
            guess = input("Gjett: ")


play_game()

        
