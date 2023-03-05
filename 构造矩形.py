import math
class Solution:
    def constructRectangle(self, area: int):
        w = math.floor(math.sqrt(area))
        print(w)
        while w>0:
            if (area % w) != 0:
                w = w -1
                print(w)
            else:
                return [(area//w),w]

so = Solution()
print(so.constructRectangle(37))
n=37%1
print(n)