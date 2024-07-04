class NumberOfIslands:
    def __init__(self, matrix):
        self.matrix = matrix

    def initialise(self):
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])
        self.queue = []
        self.dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        self.isVisited = [[False]*self.n for _ in range(self.m)]

    def navigate(self):
        count = 0
        while self.getCoordinates(self.isVisited):
            c1,c2 = self.getCoordinates(self.isVisited)
            self.isVisited[c1][c2] = True
            if self.matrix[c1][c2] == 0:
                continue
            else:
                self.queue.append((c1,c2))
                while self.queue:
                    x,y = self.queue.pop(0)
                    for dx, dy in self.dirs:
                        i = x+dx
                        j = y+dy
                        if i < 0 or i == self.m or j < 0 or j == self.n:
                            continue
                        if self.matrix[i][j] == 0 or self.isVisited[i][j]:
                            if not self.isVisited[i][j]:
                                self.isVisited[i][j] = True
                            continue
                        self.queue.append((i,j))
                        self.isVisited[i][j] = True
                count+=1
        return count

    def getCoordinates(self, booleanMatrix):
        for i in range(len(booleanMatrix)):
            for j in range(len(booleanMatrix[0])):
                if not booleanMatrix[i][j]:
                    return i,j

n = NumberOfIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]])
n.initialise()
print(n.navigate())
        


