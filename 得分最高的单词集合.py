from collections import defaultdict
from typing import List
from itertools import combinations
from copy import deepcopy
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        #筛除不在letters中单词
        # for i in words[0:]:
        #     for j in i:
        #         if j not in letters:
        #             words.remove(i)
        #声明letters字典，统计字母剩余出现次数
        dicletters = defaultdict(int)
        for i in letters:
            dicletters[i] += 1
        temp = defaultdict(int)
        # print(dicletters)
        #声明scores字典
        #不用字典，直接用score[ord('字母值')-97]
        #print(score[ord('c')-97])
        #列举可能组合
        wordscomb = []
        for i in range(1,len(words)+1):
            for j in list(combinations(words,i)):
                wordscomb.append(''.join(j))        
        #遍历组合，符合lettes字典值大于=0就进行取最大操作
        res = 0  
        for i in wordscomb:
            ans = 0
            temp = deepcopy(dicletters) 
            for j in i:
                temp[j] -= 1
                print(temp)
                if temp[j] < 0:
                    ans = 0
                    break
                else:
                    ans += score[ord(j)-97]
            #判断完这个排列，满足letters字典

            res = max(res,ans)
        return res


# words = ["dog","cat","dad","good"] 
# letters = ["a","a","c","d","d","d","g","o","o"] 
# score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

words = ["aadc","cbeaa","adcec","ccea","eacca","acee"]
letters = ["b","b","b","c","c","c","d","d","d","d","d","d","d","e","e","e"]
score = [5,10,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

s = Solution()
print(s.maxScoreWords(words,letters,score))