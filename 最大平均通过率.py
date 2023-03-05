from typing import List
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        initialrate = []
        res = 0
        numsofclass = len(classes)
        for i in classes:
            initialrate.append([i[0]/i[1]-(i[0]+1)/(i[1]+1),i[0],i[1]])
        heapq.heapify(initialrate)
        for i in range(extraStudents):
            max = heapq.heappop(initialrate)
            max[1] += 1
            max[2] += 1
            max[0] = max[1]/max[2]-(max[1]+1)/(max[2]+1)
            heapq.heappush(initialrate,max)
                
            # heapq.heapreplace
        print(initialrate)
        for j in initialrate:

            res = res + j[1]/j[2]
        res = res / numsofclass
        return res

s = Solution()
classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
print(s.maxAverageRatio(classes,extraStudents))

