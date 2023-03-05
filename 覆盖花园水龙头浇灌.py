from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
    #dp[i][j]代表起始点i到终止点j的覆盖范围
    #dp＝[[0]*(n+1) for _ in range(n+1)
    #dp ＝ {}
        res = [0 for _ in range( n + 1)]
        print(res)
    #dp[0]=(-ranges[0],ranges[0])
        for pos,val in enumerate(ranges):
            if val == 0:
                continue
            mintemp=pos-val
            maxtemp=pos+val
            print(mintemp,maxtemp)
            i = 0
            for i in range( n + 1):
                if i >= mintemp and i <= maxtemp:
                    res[i] = 1

            # res[mintemp:maxtemp+1]  = [1]*(maxtemp-mintemp+1)
            print(res)
        for i in range( n + 1):
            if res[i] == 0:
                return -1 
        return 1
s = Solution()
print(s.minTaps(3,[0,0,0,0]))