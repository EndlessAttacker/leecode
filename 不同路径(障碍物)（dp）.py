class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1]*n] + [[1]+[0]*n-1 for _ in range(m-1)]
        print(dp)
    
    # def uniquePaths(self, m, n):

    #     dp=[[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
    #     print(dp)  
    #     for i in range(1,m):
    #         for j in range(1,n):
    #             print(111)
    #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #             # print(dp[i][j])

    #     return dp[m-1][n-1]
# class Solution:
#     def uniquePaths(self, m, n):
#         f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
#         print(f)
#         for i in range(1, m):
#             for j in range(1, n):
#                 f[i][j] = f[i - 1][j] + f[i][j - 1]
#         return f[m - 1][n - 1]

s = Solution()
print(s.uniquePathsWithObstacles)