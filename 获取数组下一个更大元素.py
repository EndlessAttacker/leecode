class Solution:
    def nextGreaterElement(self,nums):
        if len(nums) == 0:
            return []
        res = []
        res2 = []
        stack = []
        tmp_nums = nums + nums
        length = len(tmp_nums)
        for j in range(length - 1,-1,-1):
            # print(stack)
            while len(stack) != 0 and stack[-1] <= tmp_nums[j]:
                stack.pop()
            if len(stack) == 0:
                cur = -1
            else:
                cur = stack[-1]         
            res.append(cur)
            stack.append(tmp_nums[j])
        res.reverse()
        for i in range(length//2):
            res2.append(res[i])

        return res2

s = Solution()
print(s.nextGreaterElement([1,3,4,3]))
        
