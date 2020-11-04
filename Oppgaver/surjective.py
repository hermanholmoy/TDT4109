import matplotlib.pyplot as plt

r1 = 1
r2 = 2000


def f(x):
    return (x) % 1729


def g(x):
    return x**2


x = [i for i in range(r1, r2)]
y = [f(i) for i in x]


def injective(x, y):
    if len(set(y)) != len(y):
        return False
    else:
        return True


def surjective(x, y):
    r1r2 = range(r1, r2)
    if len(set(y)) == len(r1r2):
        print()


print(surjective(x, y))

plt.plot(x, y)
plt.show()
