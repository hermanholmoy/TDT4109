def triangle(n):
    for i in range(1, n + 1):
        print("* " * i)


def flipped_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)


def isosceles_triangle(n):
    for i in range(1, n + 1):
        padding = " " * (n - i)
        txt = "* " * i
        print(padding + txt)


isosceles_triangle(50)
