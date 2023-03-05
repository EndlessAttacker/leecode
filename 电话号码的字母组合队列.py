from collections import deque
class Solution:
    def letterCombinations(self, digits):
        dic = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        if digits == "":
            return []
        deq = [""]
        for digit in digits:
            for _ in range(len(deq)):
                num = deq.pop(0)
                print(num)
                for i in dic[ord(digit)-50]:
                    deq.append(num+i)
        return deq

s = Solution()
print(s.letterCombinations("23"))


