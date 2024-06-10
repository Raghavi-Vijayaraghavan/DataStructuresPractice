def smallestInList(testList):
    recordSmallest = testList[0]
    for i in range(1,len(testList)):
        if(i < len(testList)):
            if(testList[i] < recordSmallest):
                recordSmallest = testList[i]
    return recordSmallest
print(smallestInList([23, 7, 41, 10, 101, 2]))
