def initialise(matrix):
    m = len(matrix)
    n = len(matrix[0])
    qA = []
    qP = []
    intoA = [[False]*n for _ in range(m)]
    intoP =  [[False]*n for _ in range(m)]
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]

    for i in range(m):
        qP.append((i,0))
        intoP[i][0] = True
        qA.append((i,(n-1)))
        intoA[i][n-1] = True

    for j in range(n):
        qP.append((0,j))
        intoP[0][j] = True
        qA.append(((m-1),j))
        intoA[m-1][j] = True

    return qA,qP,intoA,intoP,dirs


def navigate(queueX, intoX, matrix, dirs):
    m = len(matrix)
    n = len(matrix[0])
    while queueX:
        x,y = queueX.pop(0)
        h = matrix[x][y]
        for dx,dy in dirs:
            i = x+dx
            j = y+dy
            if i < 0 or i == m or j < 0 or j == n:
                continue
            if intoX[i][j] or matrix[i][j] < h:
                continue
            intoX[i][j] = True
            queueX.append((i,j))
    return intoX

def resultCoordinates(into1, into2, matrix):
    result = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if into1[i][j] and into2[i][j]:
                result.append((i,j))
    return result

inputMatrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
qA,qP,intoA,intoP,dirs = initialise(inputMatrix)
intoA = navigate(qA,intoA,inputMatrix,dirs)
intoP = navigate(qP,intoP,inputMatrix,dirs)
print(resultCoordinates(intoA,intoP,inputMatrix))
    
            
    
        
        
