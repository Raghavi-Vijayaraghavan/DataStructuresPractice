def sumOfAListOfNumbers(testList):
    if len(testList) == 1:
        return testList[0]
    else:
        return testList[0] + sumOfAListOfNumbers(testList[1:])

print(sumOfAListOfNumbers([1,2,3]))
