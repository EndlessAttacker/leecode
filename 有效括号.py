from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')' , '{':'}', '[':']'}
        stack = deque()
    
        for i in s:
            if i in dic.keys():
                    # print(dic.keys())
                stack.append(i)
                # print(stack)
            else:
                if not stack:
                    return False
                elif dic[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
                
                #     if dic[stack[-1]] == i :
                #         stack.pop()
                #     else:
                #         print(stack)
                #         return False
        if not stack:
            return True
        else:
            return False
s = Solution()
print(s.isValid(''))


