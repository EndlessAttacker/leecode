class Solution:
    def alertNames(self, keyName, keyTime):
        res = []
        dic = {}
        for i in range(len(keyName)):
            keyTime[i] = int(keyTime[i][0:2])*60 + int(keyTime[i][3:5])         
            dic.setdefault(keyName[i],[]).append(keyTime[i])
        for key,val in dic.items():
            length = len(val)
            if length < 3:
                break
            else:
                val.sort()

                for i in range(length-2):
                    if val[i+2] - val[i] <= 60:
                        res.append(key)
                        break

        res.sort()
        print(dic)
        return res

s = Solution()
keyName = ["a","a","a","a","a","a","a","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c"]
keyTime = ["00:37","11:24","14:35","21:25","15:48","20:28","07:30","09:26","10:32","20:10","19:26","08:13","01:08","15:49","02:34","06:48","04:33","07:18","00:05","06:44","13:33","04:12","03:54"]
print(s.alertNames(keyName,keyTime))