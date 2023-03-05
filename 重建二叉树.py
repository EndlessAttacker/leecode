class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) ==1:
            return TreeNode(preorder[0])
        else:
            root = inorder.index(preorder[0])
            res = TreeNode(preorder[0])
            res.left = self.buildTree(preorder[1:1+root],inorder[:root])
            res.right = self.buildTree(preorder[root+1:],inorder[root+1:])
        return res


# pre = create_tree(None,[3,9,20,15,7],0)
# ino = create_tree(None,[9,3,15,20,7],0)
s = Solution()
print(s.buildTree([3,9,20,15,7],[9,3,15,20,7]).val)