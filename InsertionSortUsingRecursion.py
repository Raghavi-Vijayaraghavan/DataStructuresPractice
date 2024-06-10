def insertionSort(a, index):
    if index == len(a):
        return a
    else:
        if index > 0:
            for i in range(index, len(a)):
                temp = a[i]
                j = i - 1
                while j>=0 and a[j] > temp:
                    a[j+1] = a[j]
                    j -= 1
                a[j+1] = temp
        return insertionSort(a, index+1)

print(insertionSort([10, 8, 7, 50, 60, 3, 9, -1], 0))
