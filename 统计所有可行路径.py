from typing import List
import functools
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int):
        @functools.lru_cache(None)
        def dfs(pos,leftOil):
            if abs(locations[finish] - locations[pos]) > leftOil:
                return 0
            res = 0
            for key,val in enumerate(locations):
                if key != pos:
                    temp = abs(val - locations[pos])
                    if temp <= leftOil:
                        res += dfs(key,leftOil - temp)
            if pos == finish:
                res += 1
            return res % 1000000007
        return dfs(start,fuel)

s = Solution()
locations = [1,2,3] 
start = 0
finish = 2
fuel = 40
print(s.countRoutes(locations,start,finish,fuel))
