def containsDuplicate(nums):
        for i in range(1, len(nums)):
            if nums[0] == nums[i]:
                return True
        return False

print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,2,3,4,1]))
