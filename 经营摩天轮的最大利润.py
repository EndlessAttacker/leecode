from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        #先判断
        if 4*boardingCost<=runningCost:
            return -1
        #后续只用考虑拉满能盈利情况
        res = count = 0
        localprofit = maxprofit = localpeople = waitpeople = 0
    
        #在customers还有，waitpeople能从customers中取时
        for i in customers:
            #每来一次，轮转次数+1
            count+=1
            #先+判断了再-
            waitpeople += i 
            localpeople = min(waitpeople,4)
            waitpeople -= localpeople
            #计算当前利润，然后和最大利润进行比较，满足了就更新最小轮转次数
            localprofit += localpeople*boardingCost - runningCost

            if  localprofit > maxprofit:
                maxprofit = localprofit
                res = count
   
        #当遍历完customers后
        #贪心
        if waitpeople>0:
            res = len(customers)
        count = waitpeople//4
        localpeople = waitpeople-4*count

        res += count
        #防止出现[0,0,0,4]这类情况
        maxprofit += (4*boardingCost - runningCost)*count
        if maxprofit<=0:
            res = -1
        if localpeople*boardingCost - runningCost>0:
            res+=1
        return res
customers = [0,0,0,4]
boardingCost = 1
runningCost = 1
s = Solution()
print(s.minOperationsMaxProfit(customers,boardingCost,runningCost))


            
                