
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # lt1 = len(text1)
        # lt2 = len(text2)
        # #dp为 lt1*lt2 长二维数组，dp[i][j]值代表text1前j个数与text2前i个数的最长公共子序列
        # dp = [[0]*(lt1+1) for i in range(lt2+1)]
        # for i in range(0,lt2+1):
        #     for j in range(0,lt1+1):
        #         #边界为0
        #         if i == 0 or j == 0:
        #             dp[i][j] = 0
        #         else:
        #             if text1[j-1] == text2[i-1]:
        #                 dp[i][j] = dp[i-1][j-1] + 1
        #             else:
        #                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
        # return dp[lt2][lt1]
        # # print(dp)
        l1, l2 = len(text1), len(text2)
        cache = [[-1] * l2 for i in range(l1)]
        # 记忆化搜索
        def dfs(i, j):
            
            # 若word1先走到最后则只能删掉word2剩余所有
            if i == l1: return l2 - j
            # word2先走到最后同理
            if j == l2: return l1 - i
            val = cache[i][j]
            if val > -1: return val
            # 两字符串当前字符相同不用管，去下一个位置
            print(i,j)
            if text1[i] == text2[j]:
                val = dfs(i + 1, j + 1)
            else:
                # 若不相同，则需要删掉一个
                # 在删word1和删word2两种决策所产生的的结果中取最小值
                val = min(dfs(i + 1, j), dfs(i, j + 1)) + 1
            cache[i][j] = val
            return val

        return dfs(0, 0)        
s = Solution()
print(s.longestCommonSubsequence('abc','d'))



