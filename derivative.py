def get_derivative(func,x):
    h = 0.0001
    return (func(x+h)-func(x))/h

def f(x): return x**2


x = 3
computed = get_derivative(f,x)
actual = 2*x # since we know derivate of x^2 is 2x

print(f"Computed : {round(computed,5)}, actual : {actual}")