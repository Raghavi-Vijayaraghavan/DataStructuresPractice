class NumArray:
    def __init__(self, inputArray):
        self.inputArr = inputArray[0]
        self.left = inputArray[1][0]
        self.right = inputArray[1][1]
        self.outputArr = []

    def sumRange(self,l,r):
        if l > r:
            return 0
        
        else:
            numsToAdd = self.inputArr[l:r+1]
            return numsToAdd[0] + self.sumRange(l+1,r)

    def outputArray(self):
        self.outputArr.append(None)
        self.outputArr.append(self.sumRange(self.left,self.right))


n = NumArray([[1,2,3,4,5], [1,3]])
print(n.outputArray())
        
