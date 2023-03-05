from typing import List
from collections import defaultdict
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        items = items1 + items2
        for [value,weight] in items:
            dic[value] += weight

        return sorted(dic.items(),key=lambda x:x[0])



items1 = [[1,1],[4,5],[3,8]] 
items2 = [[3,1],[1,5]]
s = Solution()
print(s.mergeSimilarItems(items1,items2))
