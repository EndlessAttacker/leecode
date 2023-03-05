from typing import List
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         m = len(triangle)
#         # dp = [[0]*i for i in range(1,m+1)]
#         # print(dp)
#         dp = [0] * m
#         dp[0] = triangle[0][0]
#         # print(dp)
#         for i in range(1,m):
#             for j in  range(i,-1,-1):
#                 if j > 0 and j < i:
                    
#                     dp[j] = min(dp[j],dp[j-1])
#                 elif j == i:
#                     dp[j] = dp[j-1]
#                 elif j == 0:
#                     dp[j] = dp[j] 
#                 dp[j] += triangle[i][j]
#                 print(dp[j],j)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle[-1])
        dp1 = [[0]*m]*2
        dp = [[0] * m for _ in range(2)]
        
        print(dp1==dp)        
        dp[0][0] = triangle[0][0]
        print(dp)

        for i in range(1,m):
            for j in  range(0,i+1):
                curr = i % 2
                prev = 1 - i % 2
                if j > 0 and j < i:
                    dp[curr][j] = min(dp[prev][j],dp[prev][j-1])
                elif j == i:
                    dp[curr][j] = dp[prev][j-1]
                    print(dp[curr][j]+triangle[i][j],dp[prev][j-1],dp[0][0])
                elif j == 0:
                    dp[curr][j] = dp[prev][j]
                dp[curr][j] += triangle[i][j]

        return min(dp[0])
        # res = 100000000000
        # for k in range(0,m):
        #     res = min(res,dp[m-1][k])
        # return res
        # res = 100000000000
        # for k in dp:
        #     res = min(res,k)
        # return res
        return min(dp)
s = Solution()
print(s.minimumTotal([[-10]]))


