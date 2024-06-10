a = [1,2,3,4,5]
def SumRange(left,right):
    if left > right:
        return 0
    else:
        test = a[left:right+1]
        return test[0] + SumRange(left+1, right)

print(SumRange(1,3))
