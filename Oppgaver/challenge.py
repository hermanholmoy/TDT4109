
M = 100




#a = [[()/sqrt(5) for i in range(n, n+4)] for n in range(1, M, 4)]


a = 10
tl = [1,2,3,4,7,4,10,33,4]

def c1(l):

    if len(l) == 0:
        print("Not in list")
        return -1
    else:
        if l[0] == a:
            return 0
        else:
            return 1 + c1(l[1:])



print(c1(tl))
        
