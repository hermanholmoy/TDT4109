
def calc(s):
    if "," in s:
        s.replace(",", ".")
    if s[0] != "+":
        s = "+" + s

    print(s)
    pluss = []
    minus = []
    i = 0
    curstr = ""
    while i < len(s):
        t = s[i]
        print("current type",t )

        letter = s[i+1]
        while letter not in ["+", "-"]:
            curstr += letter
            i += 1
            print("current string", curstr)
            if i < len(s):
                letter = s[i]
            else:
                break

        print("her", curstr)

        if t == "+":
            pluss.append(int(curstr))
        else:
            minus.append(int(curstr))

        i += len(curstr)
        curstr = ""
        print(i, pluss, minus)


    print(pluss)
    print(minus)

    return sum(pluss) - sum(minus)
        
        

t = "123+123-123-1+1-1"

print(calc(t))




        
