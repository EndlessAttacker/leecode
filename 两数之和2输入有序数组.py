from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        index1 = 0
        index2 = n - 1
        while index1 < n and index2 >= 1 and index1 < index2:
            if numbers[index1] + numbers[index2] < target:
                while numbers[index1 + 1] == numbers[index1]:
                    index1 += 1
                index1 += 1
            elif numbers[index1] + numbers[index2] > target:
                while numbers[index2 - 1] == numbers[index2]:
                    index2 -= 1
                index2 -= 1
            else:
                return [index1,index2]
