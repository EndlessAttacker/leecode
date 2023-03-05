class Solution:
    def fourSum(self,nums,target):
        n = len(nums)
        if not n or n<4:
            return []
        nums.sort()
        # print(nums)
        res = []
        # print(nums)
        # res = nums[n-1] + nums[n-2] + nums[n-3]
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:continue
            for j in range(i+1,n):
                if j > i + 1 and nums[j] == nums[j-1]:continue
                L = j + 1
                R = n - 1

                while L < R:

                    if nums[i] + nums[j] + nums[L] + nums[R] < target:
                        L += 1
                        # print(res,1)

                    elif nums[i] + nums[j] + nums[L] + nums[R] > target:
                        R -= 1
                    else :
                        res.append([nums[i] ,nums[j] , nums[L] , nums[R]])
                    # print(res,i,L,R)
                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        while L < R and nums[R] ==nums[R-1]:
                            R -= 1 

                        L += 1
                        R -= 1

        return res
        # nums.sort()
        # n = len(nums)
        # res = []
        # for i in range(n):
        #     if i > 0 and nums[i] == nums[i - 1]: continue
        #     for k in range(i+1, n):
        #         if k > i + 1 and nums[k] == nums[k-1]: continue
        #         p = k + 1
        #         q = n - 1

        #         while p < q:
        #             if nums[i] + nums[k] + nums[p] + nums[q] > target: q -= 1
        #             elif nums[i] + nums[k] + nums[p] + nums[q] < target: p += 1
        #             else:
        #                 res.append([nums[i], nums[k], nums[p], nums[q]])
        #                 while p < q and nums[p] == nums[p + 1]: p += 1
        #                 while p < q and nums[q] == nums[q - 1]: q -= 1
        #                 p += 1
        #                 q -= 1
        # return res


s = Solution()
resp = s.fourSum([1,0,-1,0,-2,2],0)
print(resp)