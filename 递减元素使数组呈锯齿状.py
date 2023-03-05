from math import inf
from typing import List
from copy import deepcopy

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        ans1 = 0
        ans2 = 0
        res = 0
        nums2 = deepcopy(nums)         
        nums.append(inf)
        # nums.append(inf)
 
        nums2.insert(0,inf)
        nums2.append(inf)
        print(nums,nums2)

    
        #情况1
        for i in range(1,n,2):
            if nums[i]>=nums[i+1] or nums[i]>=nums[i-1]:
                ans1 = ans1 + nums[i] - min(nums[i-1],nums[i+1]) + 1
                print('情况1',nums[i] - min(nums[i-1],nums[i+1]) + 1)
        #情况2
        for i in range(1,n+1,2):
            if nums2[i]>=nums2[i+1] or nums2[i]>=nums2[i-1]:
                ans2 = ans2 + nums2[i]-min(nums2[i-1],nums2[i+1])  + 1  
                print('情况2',nums2[i]-min(nums2[i-1],nums2[i+1])  + 1 )
            # print(i) 
        return min(ans1,ans2)


s = Solution()
print(s.movesToMakeZigzag([2,7,10,9,8,9,111]))