class Solution:
    def uniquePaths(self, m, n):

        dp=[[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(dp)  
        for i in range(1,m):
            for j in range(1,n):
                print(111)
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                # print(dp[i][j])

        return dp[m-1][n-1]
# class Solution:
#     def uniquePaths(self, m, n):
#         f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
#         print(f)
#         for i in range(1, m):
#             for j in range(1, n):
#                 f[i][j] = f[i - 1][j] + f[i][j - 1]
#         return f[m - 1][n - 1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        # print(dp)
        if m == 0 and n == 0 :
            return 1
        
        for i in range(0,m):
            for j in range(0,n):
                #初始条件
                if i == 0 and j ==0 :
                    dp[i][j] = 1
                # 情况2
                elif i ==0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j]
                elif i > 0 and j >0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(dp)
        return dp[m-1][n-1]
s = Solution()
print(s.uniquePaths(4,3))

