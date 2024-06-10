def sumOfDigits(number):
    if len(str(number)) == 1:
        total = 0
        return total + number
    else:
        numStr = str(number)
        total = int(numStr[:1]) + sumOfDigits(int(numStr[1:]))
        return total

print(sumOfDigits(1234567))
