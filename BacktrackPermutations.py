def backtrackPermutations(origList, index):
    if index == len(origList):
        print(origList)
    else:
        for i in range(index, len(origList)):
            origList[i], origList[index] = origList[index], origList[i]
            backtrackPermutations(origList, i+1)
            origList[i], origList[index] = origList[index], origList[i]
            
origList = [1,2,3]
backtrackPermutations(origList, 0)          
            
            
