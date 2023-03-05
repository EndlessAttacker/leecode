class Solution:
    def letterCombinations(self, digits) :
        dic = {"1":[],
        "2":['a','b','c'],
        "3":['d','e','f'],
        "4":['g','h','i'],
        "5":['j','k','l'],
        "6":['m','n','o'],
        "7":['p','q','r','s'],
        "8":['t','u','v'],
        "9":['w','x','y','z']}
        if digits=="" or digits == None:
            return [] 
        def dfs(Combinations,nextdigits):

            if len(nextdigits)==0:
                res.append(Combinations)
            else:
                for i in dic[nextdigits[0]]:

                    print(Combinations)
                    
                    dfs(Combinations+i,nextdigits[1:])
        res = []
        dfs("",digits)
        return res
s = Solution()
print(s.letterCombinations('23'))