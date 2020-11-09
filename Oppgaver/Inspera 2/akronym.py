def input_strings():
    l = []
    for i in range(4):
        n = input("Skriv inn en streng: ")
        
        l.append(n)
    return l


def acronym():
    l = input_strings()
    s = "".join(item[0].upper() for item in l)
    return s


print(acronym())