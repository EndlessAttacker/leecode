# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List,Optional
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists==[]:
            return 
        if lists==[[]]:
            return []
        temp = []
        for i in lists:
            for j in list(self.items(i)):
                temp.append(j)
        temp.sort()
        res = self.createkList(temp)
        #return temp
        return res    
    def items(self,i):
        curNode = i
        while curNode != None:
            yield curNode.val
            curNode=curNode.next
    def createkList(self,list1):
        
        if len(list1) == 0:
            return
        else:
            # 创建头结点
            self.head = ListNode(list1[0])
            # 头结点
            r = self.head  
            # 指针 
            p = self.head   
            # 逐个为 data 内的数据创建结点, 建立链表
            for i in list1[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return r

s = Solution()

print(s.mergeKLists([[1,4,5],[1,3,4],[2,6]]))