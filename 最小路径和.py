class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        # path = [(0,0) for _ in range(m*n)]
        path = [[0] * n for _ in range(m)]
        # print(path)
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]
        i = m - 1
        j = n - 1
        path[i][j] = 1
        while i != 0 or j != 0:
            if i == 0 : j -= 1
            elif j == 0 : i -= 1
            else:
                if dp[i-1][j] < dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
            path[i][j] = 1
        print(path)
        return dp[m-1][n-1]




s = Solution()
print(s.minPathSum([[1,2,1],[1,1,1]]))