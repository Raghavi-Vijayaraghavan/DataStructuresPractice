def backtrackCombinations(inputArray, temp, index, k):
    if len(temp) == k:
        print(temp)
    else:
        for i in range(index, len(inputArray)):
            temp.append(inputArray[i])
            backtrackCombinations(inputArray, temp, i+1, k)
            temp.pop(-1)

inputArray = [1,2,3,4]
k = 3
temp = []
backtrackCombinations(inputArray, temp, 0, k)
