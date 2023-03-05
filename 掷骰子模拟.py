from typing import List
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # i:剩余次数；  last：前一个骰子数连续出现的次数；  left：前一个骰子数剩下可以出现的次数
        def dfs(i: int, last: int, left: int) -> int:
            if i == 0: return 1
            res = 0
            #j：骰子点数；mx：j点数对应的最大连续出现数
            for j, mx in enumerate(rollMax):
                #不等于上个骰子数情况，last改为j，同时mx-1    
                if j != last: 
                    res += dfs(i - 1, j, mx - 1)
                #等于上个骰子数情况，同时判断是否还能继续出现上个数字，还能就继续
                elif left: 
                    res += dfs(i - 1, j, left - 1)
            return res % MOD
        return sum(dfs(n - 1, j, mx - 1) for j, mx in enumerate(rollMax)) % MOD

s = Solution()
n = 2
rollMax = [1,1,2,2,2,3]
print(sum(rollMax))
print(s.dieSimulator(n,rollMax))