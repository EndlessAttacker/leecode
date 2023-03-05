class Solution:
    def getMaximumConsecutive(self, coins):
        coins.sort()
        ans=1
        for i in coins:
            if i >ans:
                break
            ans = ans+i
        return ans

s = Solution()
print(s.getMaximumConsecutive([1,2,3]))