def y(x):
    print("$"* x)
    if x > 1:
        y(x-1)
    print("$"*x)

y(5)
