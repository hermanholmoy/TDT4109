def correct_word(word):
    for letter in word:
        if not letter.isalpha():
            return False
    else:
        return True


def count_letters(word):
    if correct_word(word):
        return len(word)

    else:
        return -1


print(count_letters("Herman"))
print(count_letters("ITGK<3"))