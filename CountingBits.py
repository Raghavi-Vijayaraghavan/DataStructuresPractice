def countBits(n):
    if n <= 0:
        return 0
    if n in [1,2]:
        return 1
    else:
        return countBits(n-1) + (2*(countBits(n-1)+1)) + (countBits(n-1) + 2)

print(countBits(8))
