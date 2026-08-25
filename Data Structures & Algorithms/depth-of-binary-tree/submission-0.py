# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_depth(self,root,h,max_h):
        if(root==None):
            return max_h
        max_h = max(h,max_h)
        max_h = self.max_depth(root.left,h+1,max_h)
        max_h = self.max_depth(root.right,h+1,max_h)
        return max_h
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_h = self.max_depth(root,1,0)
        return max_h
        