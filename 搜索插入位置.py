from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        temp = (left+right)//2
        while left<right:
            if nums[temp]>=target:
                right = temp
                temp  = (left+right)//2
                print(left,right,temp)
            elif nums[temp]<=target:
                left = temp
                temp  = (left+right)//2
                print('1',left,right,temp)
            if right-left<=1:
                break
        if target<=nums[left]:
            return left
        elif target>nums[left] and target<=nums[right]:
            return right
        else:
            return right+1


s = Solution()
nums = [1,3,5,6]
target = 2
print(s.searchInsert(nums,target))