class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        res = ""
        startx = 0
        starty = 0
        for i in target:
            ix = (ord(i)-ord('a')) % 5
            iy = (ord(i)-ord('a')) // 5
            # return ix,iy
            if ix < startx :
                res += "L" * (startx-ix)               
            if iy > starty :
                res += "D" * (iy-starty)        
            if iy < starty :
                res += "U" * (starty-iy)                       
            if ix > startx :
                res += "R" * (ix-startx)            
            res += '!'
            startx = ix
            starty = iy
        return res

s = Solution()
dp = [[0]*3]*2
print(dp)
print(s.alphabetBoardPath("zbz"))


