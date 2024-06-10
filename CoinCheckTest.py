
def f(sumVar):
    if sumVar < min([2,5]):
        return 0
    elif sumVar in [2,5]:
        count = 0
        for i in [2,5]:
            if sumVar%i == 0:
                count+=1
        return count
    else:
        return f(sumVar-5) + f(sumVar-2)

for k in range(10):
    print(k, f(k))
