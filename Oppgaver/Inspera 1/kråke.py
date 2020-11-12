def ask_question(spm):
    svar = input(spm)
    return svar


# pørsmål = input("Spørsmål: ")
# svar = ask_question(spørsmål)
# print(svar)


def spam_with_questions(spm):
    while True:
        inp = input(spm)
        if inp.lower() == "stopp":
            break


def energy_efficient_spamming(str1, str2):
    if len(str1) < len(str2):
        return None

    svar = input(str1)
    if svar != "stopp":
        spam_with_questions(str2)


energy_efficient_spamming("Hvor lenge er det igjen? ", "Nå da? ")
