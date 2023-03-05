from typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        length = len(hours)
        res = 0
        score = [0] * length
        ans = []
        for i in range(length):
            left = 0 
            if hours[i] > 8:
                score[i] = 1
            elif hours[i] <= 8:
                score[i] = -1
        sum = 0
        for j in score:
            ans.append(sum)
            sum += j
        ans.append(sum)
        res = 0

        stack = []
        for i in range(length+1):
            while  stack == [] or ans[i] < ans[stack[-1]]:
                stack.append(i)
        print(stack)

        for j in range(length,-1,-1):
            while len(stack)>0 and ans[stack[-1]] < ans[j]:
                res = max(res,j - stack[-1])
                stack.pop()
        # for left in range(length):
        #     for right in range(length,left,-1):
        #         if ans[right]-ans[left] > 0:
        #             res = max(res,right-left)
        #             continue

        return res

s = Solution()
days = [6,9,9,9,6,9,6,6]
print(s.longestWPI(days))
















        #     count1 = count
        #     while left < right and count1 < 1:
        #         if hours[left] > 8:          
        #             count1 -= 1
        #         else:
        #             count1 += 1             
        #         left += 1
        #     if count1 >= 1:
        #         res = max(res,right - left + 1)
        # return res

