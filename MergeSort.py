def msDivide(a):
    if len(a) <= 1:
        return a
    else:
        mid = len(a)//2
        lHalf = a[:mid]
        rHalf = a[mid:]
        leftElements = msDivide(lHalf)
        rightElements = msDivide(rHalf)
        return msMerge(leftElements, rightElements)

def msMerge(l,r):
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    res.extend(l[i:])
    res.extend(r[j:])
    return res

print(msDivide([5,4,3]))
