# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def find_balance(self,root):
        if(root==None):
            return 0
        left_h = self.find_balance(root.left)
        right_h = self.find_balance(root.right)
        if(left_h ==-1 or right_h==-1):
            return -1
        if(abs(left_h-right_h)>1):
            return -1
        return 1+max(left_h,right_h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = self.find_balance(root)
        if(ans==-1):
            return False
        return True