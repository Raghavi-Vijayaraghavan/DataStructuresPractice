def printPermutations(origSet, temp, index):
    if temp == origSet:
        return
    if index == len(temp)-1:
        index = 0
    if not temp:
        temp = origSet[:]
    temp[index], temp[index+1] = temp[index+1], temp[index]
    print(temp)
    printPermutations(origSet, temp, index+1)

origSet = [1,2,3,4]
temp = []
printPermutations(origSet, temp,0)
