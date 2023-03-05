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
    def pathSum(self, root, target):
        if not root:
            return []
        



arraylist = [1,2,3]
s=create_tree(None,arraylist,0)
res= Solution()
print(res.btreeGameWinningMove(s,3,1))
