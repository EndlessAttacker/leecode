class Solution:
    def removeSubfolders(self, folder):
        if not folder:
            return []
        n = len(folder)
        folder.sort()
        res = [folder[0]]

        for i in range(1,n):
                # print(folder[i].split('/'))
            # if folder[i].split(res[-1]) != "":
            #     res.append(folder[i])
            # else
            B = folder[i].split('/')
            A = res[-1].split('/')
            if  not any([A==B[i:i+len(A)] for i in range(0,len(B)-len(A)+1)]):
                res.append(folder[i])

        return res









str1 = "/a/b/c"
str = ["/a","/a/b","/c/d","/c/de/e","/c/f"]
s = Solution()
# print(str1.split('/'))
print(s.removeSubfolders(str))