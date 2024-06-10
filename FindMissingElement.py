def findMissingElement(nums):
    for i in range(len(nums)+1):
        if not i in nums:
            return i
        
print(findMissingElement([0]))
