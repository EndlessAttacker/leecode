from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sum = 0
        for i in range(10):
            sum+=i
        print(sum)
s = Solution()
print(s.isValidSudoku([1,3]))