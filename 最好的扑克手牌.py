from typing import List
from collections import defaultdict
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        else:
            dic = defaultdict(int)
            for i in ranks:
                dic[i] += 1
            res = 0
            for key,val in dic.items():
                res = max(val,res)
            if res >= 3:
                return "Three of a Kind"
            elif res == 2:
                return "Pair"
            else:
                return "High Card"
            # if max(dic.values)
s = Solution()
ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]
print(s.bestHand(ranks,suits))