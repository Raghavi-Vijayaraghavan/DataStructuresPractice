def fibonacciSequence(n1, n2, stopNumber):
    count = stopNumber
    if count == 0:
        return "End"
    else:
        print(n1 + n2, end = ' ') 
        count = count - 1
        return fibonacciSequence(n2, n1+n2, count)

print(fibonacciSequence(0, 1, 10))
