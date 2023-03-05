from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        s = 1
        res = 0
        res1 =[]
        if k <= 1:
            return 0
        for right,val in enumerate(nums):
            s = s * val
            # print(s,right)
            while s >= k:
                s = int(s/nums[left])
                left += 1

            res += right - left + 1
            # print(right,res)
        
        return res



s = Solution()
print(s.numSubarrayProductLessThanK([1],1))