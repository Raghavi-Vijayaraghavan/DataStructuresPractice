def findMinCost(k,l):
    i,j = k,l
    if k == M and l == N:
        print('Reached ' + str(k,l))
    else:
        if k <= len(Matrix)-2 and l <= len(Matrix[k])-2 :
            j = l+1
            i = k+1
            temp = Matrix[k][j]
            if Matrix[i][l] < temp:
                temp = Matrix[i][l]
                k,l = i,l
                print(str(k),str(l) + '--> ')
            if Matrix[i][j] < temp:
                temp = Matrix[i][j]
                k,l = i,j
                print(str(k),str(l) + '--> ')
            k,l = k,j
            print(str(k),str(l) + '--> ')
        if l == len(Matrix[k])-1:
            j = l+1
            k,l = k,j
            print(str(k),str(l) + '--> ')
        if k == len(Matrix)-1:
            i = k+1
            k,l = i,l
            print(str(k),str(l) + '--> ')
        findMinCost(k,l)

Matrix = [[1,2,3],[4,8,2],[1,5,3]]
M,N = 2,2
findMinCost(0,0)
