def divideArray(a):
    if len(a) == 1:
        return a
    else:
        half = len(a)//2
        lHalf = a[:half]
        rHalf = a[half:]
        leftArray = divideArray(lHalf)
        print(leftArray)
        rightArray = divideArray(rHalf)
        return leftArray


#def mergeArrayElements()        
print(divideArray([1,2,3,4]))
