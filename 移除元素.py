from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[j] = nums[i]
        #         j += 1
        # for i in range(len(nums) - 1, j - 1, -1):
        #     nums.pop(i)
        # print(nums)
        # return j
        i = 0
        n = len(nums)
        j = n-1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j-=1
            else:
                i += 1
        return i
s = Solution()
nums = [3,2,2,3,5,2,7]
val = 3
print(s.removeElement(nums,val))