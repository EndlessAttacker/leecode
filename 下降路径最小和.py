from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        dp = [[0 for n in range(length)] for m in range(length) ]
        print(dp)
        dp[0] = matrix[0]
        for i in range(1,length):
            for j in range(length):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j+1]) + matrix[i][j]
                    # print(dp[i-1][j],dp[i-1][j+1])
                if j > 0 and j < length - 1:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1]) + matrix[i][j]
                if j == length - 1:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + matrix[i][j]

        return min(dp[-1])





s = Solution()
matrixlive = [[2,1,3],[6,5,4],[7,8,9]]
print(s.minFallingPathSum(matrixlive))
