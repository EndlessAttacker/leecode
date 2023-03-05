from collections import deque
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
##数组
# class Solution:
#     def levelOrder(self, root):
#         if root == None:
#             return None
#         level = [root]
#         list = [[] for _ in range(1000) ]
#         while level:
#             newlevel=[]
#             depth = 0
#             for i in level:
                
#                 if i.left:
#                     newlevel.append(i.left)
#                 if i.right:
#                     newlevel.append(i.right)
#                 for _ in range(len(newlevel)):
#                     list[depth].append(i.val)
#                 depth += 1
#             level = newlevel
#         return list
#栈队列               
class Solution:
    def levelOrder(self, root):
        if root == None:
            return None
        level = deque()
        level.append(root)
        list = []
        depth = 0
        while level:
            newlevl =[]
            for _ in range(len(level)):
                node = level.popleft()
                newlevl.append(node.val)
                # depth = depth + 1
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            
            list.append(newlevl)
            
            # level = newlevel
        return list

root = create_tree(None,[3,9,20,1,1,15,7],0)
# ino = create_tree(None,[9,3,15,20,7],0)
# root=TreeNode()
s = Solution()
ros = s.levelOrder(root)
print(ros)