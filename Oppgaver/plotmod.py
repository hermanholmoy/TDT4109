import matplotlib.pyplot as plt


def f(x):
    return (7*x) % 1729


x = []
y = []

for i in range(0, 2000):
    x.append(i)
    y.append(f(i))


plt.plot(x, y)
plt.show()
