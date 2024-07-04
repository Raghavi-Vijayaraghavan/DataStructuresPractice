class WordSearch:
    def __init__(self, board, word):
        self.board = board
        self.word = word
        self.m = len(board)
        self.n = len(board[0])

    def dfs(self,i,j,k):
        if i < 0 or j < 0 or i == self.m or j == self.n:
            return False
        if self.board[i][j] != self.word[k] or self.board[i][j] == '#':
            return False
        if k == len(self.word)-1:
            return True
        temp = self.board[i][j]
        self.board[i][j] = '#'
        result = self.dfs(i+1, j, k+1) or self.dfs(i, j+1, k+1) or self.dfs(i-1, j, k+1) or self.dfs(i, j-1, k+1)
        self.board[i][j] = temp
        return result

    def callDfs(self):
        result = any(self.dfs(i,j,0) for i in range(self.m) for j in range(self.n))
        return result

w = WordSearch([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], 'BFIHG')
print(w.callDfs())
        
