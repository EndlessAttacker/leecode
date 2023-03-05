class Solution:
    def isUnique(self, astr: str) -> bool:
        for i in astr:
            astr = astr[1:]
            
            print(astr)
            if i in astr:       
                return False

        return True
s = Solution()
print(s.isUnique("abv"))