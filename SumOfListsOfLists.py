def sumOfListOfLists(testList):
    if len(testList) == 1:
        return testList[0]
    else:
        if isinstance(testList[0], int):
            return testList[0] + sumOfListOfLists(testList[1:])
        else:
            return sumOfListOfLists(testList[0])

print(sumOfListOfLists([1,2, [1,2,3,4], [1,2,3], 2]))
