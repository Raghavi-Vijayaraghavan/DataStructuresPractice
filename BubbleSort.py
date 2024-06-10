def bubbleSort(testList):
    for i in range(len(testList),0,-1):
        for j in range(0, i-1):
            if(testList[j] > testList[j+1]):
                testList[j], testList[j+1] = testList[j+1], testList[j]
    
    return testList
print('SortedList', bubbleSort([64, 34, 25, 12, 22, 11, 90]))
