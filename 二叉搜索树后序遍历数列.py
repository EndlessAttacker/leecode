# class Solution:
    # def verifyPostorder(self, postorder):
    #     if not postorder:
    #         return True
    #     # 后序遍历根节点肯定在最后面
    #     root = postorder[-1]
    #     # 左半结点都比根结点小，右半部分都比根结点大
    #     n, ind = len(postorder), 0
    #     while ind < n and postorder[ind] < root:
    #         ind += 1
    #     for j in range(ind, n - 1):
    #         if not postorder[j] > root:
    #             return False
    #     return self.verifyPostorder(postorder[:ind]) and self.verifyPostorder(postorder[ind:-1])
class Solution:
    def verifyPostorder(self, postorder):
        if not postorder:
            return True
        n = len(postorder)
        root = postorder[-1]

        flag = 0
        for i in range(n):
            if postorder[i] < root:
                flag += 1
            else:
                break
        for j in range(flag,n-1):
            if postorder[j] < root:
                return False
        return self.verifyPostorder(postorder[:flag]) and self.verifyPostorder(postorder[flag:-1])

s = Solution()
print(s.verifyPostorder([]))
