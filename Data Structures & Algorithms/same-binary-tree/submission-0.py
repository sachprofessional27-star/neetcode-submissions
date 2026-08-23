# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self,n1,n2,flag):
        if(n1==None):
            if(n2!=None):
                flag = False
                return flag
            else:
                return flag
        if(n2==None):
            if(n1!=None):
                flag = False
                return flag
            else:
                return flag 
        if(n1.val!=n2.val):
            flag = False
            return flag
        flag = self.rec(n1.right,n2.right,flag)
        flag = self.rec(n1.left,n2.left,flag)
        return flag
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = self.rec(p,q,True)
        return flag
        