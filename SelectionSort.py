def selectionSort(testList):
    smallest = testList[0]
    for i in range(1, len(testList)):
        if(i < len(testList)):
            for j in range(i+1,len(testList)):
                if (testList[j] < testList[i]):
                    smallest = testList[j]
                    testList[i], smallest = smallest, testList[i]            
   
    return testList

print('Sorted List', selectionSort([23, 7, 41, 0, 101, 2]))
            
            
                
