def printSubsets(mainset, index, paths, result):
    print(paths)
    result.append(paths)
    for i in range(index, len(mainset)):
        paths.append(mainset[i])
        printSubsets(mainset, i+1, paths, result)
        paths.pop(-1)
    

paths = []
result = []
printSubsets([1,2,3], 0, paths, result)    
