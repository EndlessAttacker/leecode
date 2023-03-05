from filecmp import cmp


class Solution:
    def dicInclusion(self, s1: str):
        dic = {}
        for i in s1:
            if dic.get(i) == None:
                dic.update({i:1})
            else:
                dic[i] += 1
        return dic

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # for i in s1:
        #     if dic.get(i) == None:
        #         dic.update({i:1})
        #     else:
        #         dic[i] += 1
        n1 =len(s1)
        n2 = len(s2)        
        left = 0
        right = left + n1
        ans = 0

        dics1 = self.dicInclusion(s1)
        for left in range(n2-n1+1):
            print(left)
            if s2[left] in dics1:
                # print(left,left+n1,s2[left:left+n1])
                dics2 = self.dicInclusion(s2[left:left+n1])
                print(dics1,dics2)
                if dics1 == dics2:
                    return True
                else:
                    continue
        return False                
                   
s1 = "adc"
s2 = "dcda"
s = Solution()
print(s.checkInclusion(s1,s2))