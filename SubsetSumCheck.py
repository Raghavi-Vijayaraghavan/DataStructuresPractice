def subsetSumCheck(iterable, sumVariable):
    if len(iterable) == 0:
        return False
    else:
        for i in range(1,len(iterable)):
            for j in range(len(iterable), i+1, -1):
                total = iterable[0] + sum(iterable[i:j])
                if total == sumVariable:
                    return True
        return subsetSumCheck(iterable[1:], sumVariable)
            

print(subsetSumCheck([1,2,3,4,5], 7))
    
        
