from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        res = 0
        for i in range(length-1,1,-1):
            left = 0
            right = i - 1
            while left < right: 
                if nums[left] + nums[right] <= nums[i]:
                    left += 1

                elif nums[left] + nums[right] > nums[i]:
                    #如果符合这个条件，意味着left到right这个区段[left,right)的left都是符合条件的
                    res += right - left
                    right -= 1
        return res
s = Solution()
nums = [2,2,3,4]
print(s.triangleNumber(nums))
