def combinationsSum(inputArray, temp, index, target):
    
        print(temp)
    
        for i in range(index, len(inputArray)):
            temp.append(inputArray[i])
            combinationsSum(inputArray, temp, index+1, target)
            temp.pop(-1)

inputArray = [2,3,6,7]
target = 7
combinationsSum(inputArray, [], 0, target)
