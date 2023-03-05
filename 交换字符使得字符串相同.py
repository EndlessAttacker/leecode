class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        numx = s1.count('x') + s2.count('x')
        numy = s1.count('y') + s2.count('y')
        news1 = []
        lenxy = len(s1)
        #前提总数x和总数y都必为偶数
        #顺便提前判断奇数偶数
        if numx % 2 == 1 or numy % 2 == 1:
            return -1
        for i in range(lenxy):
            if s1[i] != s2[i]:
                news1.append(s1[i])
        temp1 = news1.count('x')
        temp2 = news1.count('y')
        # temp1 = max(numxnews1,numynews1)
        # temp2 = min(numxnews1,numynews1)
        #双类元素情况
        #大鸡小鸡情况
        if temp1 % 2 == 1 and temp2 % 2 == 1:
            return int((temp1 - 1)/2 + (temp2 -1)/2 + 2)
        #大偶小偶情况
        elif temp1 % 2 == 0 and temp2 % 2 == 0:
            return int((temp1+temp2)/2 )
        # elif temp1 % 2 == 1 and temp2 % 2 == 0:
        #     return  (temp1 - 1)/2              



           
s = Solution()
s1 = 'xxxxyyyy'
s2 = 'yyyyxyyx'
print(s.minimumSwap(s1,s2))
