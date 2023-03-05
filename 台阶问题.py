import functools
class Solution:
    def waysToStep(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4,n+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000007
        return dp[n]
s = Solution()
print(s.waysToStep(5))

        # @functools.lru_cache(None)
        # def dfs(cur):
        #     if cur > n:
        #         return 0
        #     if cur == n:
        #         return 1
        #     return dfs(cur+1)+dfs(cur+2)+dfs(cur+3)
        # return dfs(0)%1000000007
