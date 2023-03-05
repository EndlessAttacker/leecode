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

def preOrder(root):
    if root == None:
        return None
    res = ""
    res = res.join(str(root.val))
    preOrder(root.left)
    preOrder(root.right)
    print(res)

class Solution:
    def mirrorTree(self, root):
        if root == None:
            return None
        root.left,root.right = root.right,root.left
        if root.left:
            self.mirrorTree(root.left)
        if root.right:
            self.mirrorTree(root.right)
        return root


root = create_tree(None,[4,2,7,1,3,6,9],0)
# ino = create_tree(None,[9,3,15,20,7],0)
# root=TreeNode()
s = Solution()
ros = s.mirrorTree(root)
print(preOrder(ros))