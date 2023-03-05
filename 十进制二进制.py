class Solution:
    
    def printBin(self, num: float) -> str:
        res = ''
        count = 0
        while num!= 0:
            num = num*2
            if num >= 1:
                num = float('0.'+ str(num).split('.')[1])
                res +='1'
                count += 1
                print(num)
            else:
                res +='0'
                count += 1
                print(num)
            if count > 30:
                res = 'ERROR'
                break
        return res
s = Solution()
print(s.printBin(3.2)) 

        