def powerSetWithoutDuplicates(origSet, index, temp, result):
    if temp not in result:
        print(temp[:])
        result.append(temp)
    for i in range(index, len(origSet)):
        temp.append(origSet[i])
        powerSetWithoutDuplicates(origSet, i+1, temp, result)
        temp.pop(-1)

result = []
temp = []
origSet = [1,2,3,4]
powerSetWithoutDuplicates(origSet, 0, temp, result)
#print(result)
