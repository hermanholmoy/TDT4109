def derivative(x, function):
    h = 10**(-8)
    return (function(x+h)-function(x))/h


def f(x):
    return x**2+2*x+13

a = derivative(3, f)

print(round(a, 2))