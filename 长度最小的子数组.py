from math import inf
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        ans = inf
        s = 0
        for right,val in enumerate(nums):
            s += val
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
                
            if s >= target:

                ans = min(ans,right-left+1)

        return ans if ans <= n else 0
            



s = Solution()
print(s.minSubArrayLen(11,[1,1,1,1,5,1]))