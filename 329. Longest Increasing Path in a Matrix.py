# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/submissions/

class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.G = []
        for index in range(self.m):
            self.G.append([0] * self.n)
        self.greatest_length = 1          
            
        for i in range(self.m):
            for j in range(self.n):
                if self.G[i][j] == 0:
                    self.update(matrix, i, j)
                    
        return self.greatest_length

    def update (self, matrix, i, j):
        sides = []
        if i-1 != -1:
            if matrix[i][j] < matrix[i-1][j]:
                sides.append((i-1,j))
        if i+1 != self.m:
            if matrix[i][j] < matrix[i+1][j]:
                sides.append((i+1,j))
        if j-1 != -1:
            if matrix[i][j] < matrix[i][j-1]:
                sides.append((i,j-1))
        if j+1 != self.n:
            if matrix[i][j] < matrix[i][j+1]:
                sides.append((i,j+1))

        if len(sides) == 0:
            self.G[i][j] = 1

        for k, l in sides:
            if self.G[k][l] == 0:
                self.update(matrix, k, l)
            if self.G[i][j] < self.G[k][l] + 1:
                self.G[i][j] = self.G[k][l] + 1
                if self.greatest_length < self.G[i][j]:
                    self.greatest_length = self.G[i][j]


def test ():
    matrix_1 = [[9,9,4],
                [6,6,8],
                [2,1,1]]

    matrix_2 = [[3,4,5],
                [3,2,6],
                [2,2,1]]

    s_1 = Solution()
    s_2 = Solution()

    print(s_1.longestIncreasingPath(matrix_1) == 4) 
    print(s_2.longestIncreasingPath(matrix_2) == 4) 

#test()