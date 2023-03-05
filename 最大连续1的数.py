from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,res = 0,0  
        ans = 0
        for right,val in enumerate(nums):
            if val == 0 :
                ans += 1                
            while left < right and ans > k:
                if nums[left] == 0:
                    ans -= 1
                left += 1
                
            # if nums[left:right+1].count(0) <= k:
            res = max(res,right-left+1)
        return res




s = Solution()
nums = [0,0,0,0]
print(s.longestOnes(nums,0))
# print(nums[0:11].count(0))