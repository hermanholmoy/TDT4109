a = "sannsynlighetstetthetsfunksjonene"
brukt = []
a = list(a)
print(len(a))

for letter in a:
    if letter not in brukt and a.count(letter) != 1:
        print(letter, a.count(letter))
        brukt.append(letter)
