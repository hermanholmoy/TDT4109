import time


def fib_performance(func, inp):
    start = time.time()
    func(inp)
    end = time.time()

    print(f"Runtime for n={inp} : ", (end - start))


def fib1(a):

    n = 1
    m = 1
    fibs = [0, 1]
    i = 0

    while i < a - 3:
        fibs.append(n)
        temp = n
        n = m + n
        m = temp
        i += 1

    print(fibs)


def fib2(ant):
    fibs = [0]

    def a(n):
        return ((1 + 5 ** (1 / 2)) / 2) ** n

    def b(n):
        return ((1 - 5 ** (1 / 2)) / 2) ** n

    def fib_n(n):
        return (a(n) - b(n)) / (a(1) - b(1))

    for i in range(ant - 1):
        fibs.append(int(round(fib_n(i), 0)))

    print(fibs)


# n = 10**3
# fib_performance(fib1, n)
# fib_performance(fib2, n)

print(fib1(20))
