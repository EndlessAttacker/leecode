from typing import List
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        length = len(nums)
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        all_nums = 0
        les_nums = 0

        for i,val in dic.items():
            if val // 2 == 0:
                les_nums += 1
            elif val // 2 > 0:
                if val % 2 == 1:
                    les_nums += 1
                all_nums += val // 2
        res = [all_nums,les_nums]
        return res


#         length = len(nums)
#         res = []
#         all_nums = 0
#         val = length
#         right = val - 1
#         # for i in range(length-1,0,-1):
#         while val > 1 and right > 0:
#             while nums[right] != nums[0]:
#                 right -= 1
#             if right == 0:
#                 break
#             if nums[right] == nums[0]:
#                 # nums = [nums for i in range(len(nums)) if i not in [0,right]]
#                 for index in reversed([0,right]):
#                     nums.pop(index)
#                 # print(nums,right,nums[0])
#                 val -= 2
#                 all_nums += 1
#                 right = val - 1
#                 print(nums,all_nums,val,right)
#             else:
#                 break
#         res=[all_nums,val]
#         return res
s = Solution()
print(s.numberOfPairs([1,0,0]))
