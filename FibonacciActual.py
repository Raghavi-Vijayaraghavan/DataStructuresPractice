def fibActual(n):
    if n<=1:
        return 0
    if n == 2:
        return 1
    else:
        return fibActual(n-1) + fibActual(n-2)

for i in range(1,7):
    print(fibActual(i))

