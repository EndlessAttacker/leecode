class Solution:
    def threeSumClosest(self, nums,target):
        n = len(nums)
        if not n or n<3:
            return []
        nums.sort()
        # print(nums)
        res = nums[n-1] + nums[n-2] + nums[n-3]
        for i in range(n):
            L = i + 1
            R = n - 1

            while L < R:

                if nums[i] + nums[L] + nums[R] == target:
                    return target

                elif nums[i] + nums[L] + nums[R] > target:
                    
                    if abs(nums[i] + nums[L] + nums[R] - target) < abs(res - target):
                        res = nums[i] + nums[L] + nums[R]
                    # print(res,i,L,R)
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] < target:

                    if abs(nums[i] + nums[L] + nums[R] - target) < abs(res - target):
                        res = nums[i] + nums[L] + nums[R]
                    L = L + 1
 
        return res
s = Solution()
resp = s.threeSumClosest([1,1,-1,0],-6)
print(resp)