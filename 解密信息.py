#from curses.ascii import SO
class Solution:
    def decodeMessage(self, key: str, message: str):
        s = ""
        key = key.replace(" ","")
        for i in key:       
            
            if i not in s:
                s = s + i
        # return s
        standerd = "abcdefghijklmnopqrstuvwxyz"
        dic= {}
        for i in range(len(s)):
            dic[s[i]] = standerd[i]
        dic[" "]=" "
        res = ""
        j = 0
        for j in message:

            res = res + dic.get(str(j))

        return res
s = Solution()
t=s.decodeMessage("the quick brown fox jumps over the lazy dog","vkbs bs t suepuv")
print(t)
