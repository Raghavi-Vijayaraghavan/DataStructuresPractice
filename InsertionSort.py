def insertionSort(testList):
    for i in range(1,len(testList)):
        for j in range(i):
            if testList[i] < testList[j]:
                testList.insert(j, testList[i])
                testList.pop(i+1)
                break
                
    return testList

print(insertionSort([5,4,3,2,1]))
        
    
