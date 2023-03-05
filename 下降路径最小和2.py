from typing import List
class Solution:
    def delJ(self,j,list):
        list2 = list.copy()
        for i in reversed(range(len(list2))):
            if i == j:
                del list2[i]
        # print(id(list),id(list2))
        print(j,list2)
        # list2 = list
        # del list2[j]
        return list2

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        length = len(grid)
        dp = [[0 for i in range(length) ] for j in range(length)]
        dp[0] = grid[0]
        for i in range(1,length):
            for j in range(length):
                dp[ i ][ j ] = min(self.delJ(j , dp[ i - 1 ])) + grid[ i ][ j ]


        return min(dp[ -1 ])


s = Solution()
print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))