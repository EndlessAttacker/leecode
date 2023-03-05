from ast import While
from tkinter import W


class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if not n or n<3:
            return []
        nums.sort()
        res = []
        for i in range(n):
            # if nums[i]>0:
            #     return res
            if i>0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i],nums[L],nums[R]])

                    while L<R and nums[i] == nums[L+1]:
                        L = L + 1
                    while L<R and nums[i] == nums[R-1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R = R - 1
                else:
                    L = L + 1
 
        return res
s = Solution()
resp = s.threeSum([1,-1,-1,0])
print(resp)
