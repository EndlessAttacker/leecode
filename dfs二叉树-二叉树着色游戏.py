class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(root,array,i):
    if i < len(array):
        if array[i] is None:
            return None
        root = TreeNode(array[i])
        root.left = create_tree(root.left,array,2*i+1)
        root.right = create_tree(root.right,array,2*i+2)
        return root
    return root
class Solution:
    def btreeGameWinningMove(self, root,n,x):  
        def dfs(root):
            if root is None:
                return 
            if root.val == x:
                return root
            # print(root.val)
            return dfs(root.left) or dfs(root.right)

        
            # nonlocal ans
            # ans = max(ans,cnt)
        def count(root):
            if root is None:
                return 0
            # if root.left is None and root.right is None:
            #     return 0
            return count(root.left) + count(root.right) + 1
            
        # nonlocal l,r
        node = dfs(root)
  
        l,r = count(node.left),count(node.right)
        print(l,r,n - count(node))
        return max(l, r, n - count(node))  > n//2
        # def dfs(root):
        #     if not root:
        #         return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     if root.val == x:
        #         self.red_left = left
        #         self.red_right = right
        #     return left + right + 1
        
        # dfs(root)
        # parent = n - self.red_left - self.red_right - 1
        # judge = [parent, self.red_left, self.red_right]
        # return any([j > n // 2 for j in judge])



arraylist = [1,2,3]
s=create_tree(None,arraylist,0)
res= Solution()
print(res.btreeGameWinningMove(s,3,1))
