# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_depth(self,root):
        if(root==None):
            return 0
        left_h = self.max_depth(root.left)
        right_h = self.max_depth(root.right)
        return 1+max(left_h,right_h)
        
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_h = self.max_depth(root)
        return max_h
        