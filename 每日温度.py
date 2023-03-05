from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        length = len(temperatures)
        res = []
        stack = []

        for j in range(length - 1,-1,-1):

            while len(stack) != 0 and temperatures[stack[-1]]  <= temperatures[j]:
                stack.pop()

            if len(stack) == 0:
                cur = 0
            else:
                cur = stack[-1] - j 

            res.append(cur)
            stack.append(j)
        res.reverse()
        return res

s = Solution()
print(s.dailyTemperatures([34,80,80,34,34,80,80,80,80,34]))