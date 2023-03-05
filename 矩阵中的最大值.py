from typing import List
class Solution:
    def getmaxij(self,grid,i,j):
        res = 0
        for x in range(i,i+3):
            for y in range(j,j+3):
                res = max(res,grid[x][y])
        return res
                

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                # res = 0
                # for x in range(i,i+3):
                #     for y in range(j,j+3):
                #         m[i][j] = max(res,grid[x][y]) 
                m[i][j] = self.getmaxij(grid,i,j)
        return m
                

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
s = Solution()
print(s.largestLocal(grid))
