from math import inf


class Solution:
    def balancedString(self, s: str) -> int:
        dic = {}
        n = len(s)
        # res = 0
        # left = 0
        # ans = 0
        for i in s:
            if dic.get(i) == None:
                dic.update({i:1})
            else:
                dic[i] += 1

        if all(dic[i] == n // 4 for i in dic):
            return 0

        else:
            left = 0
            ans = inf
            for right,val in enumerate(s):
                dic[val] -= 1
                # print(dic,right,left)
                while all(dic[i] <= (n // 4) for i in dic):
                    ans = min(ans,right - left + 1)
                    dic[s[left]] += 1
                    left += 1
                    
            return ans





s = Solution()
print(s.balancedString("QEWRR"))