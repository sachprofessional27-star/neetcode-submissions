# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self,root,s):
        if root is None:
            return 0,s
        left,s = self.rec(root.left,s)
        right,s = self.rec(root.right,s)
        node = left+right+root.val
        if node>s:
            s = node

        if left+root.val<0 and right+root.val<0:
            return 0,s
        if left>right:
            return root.val+left,s
        else:
            return root.val+right,s
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s = float('-inf')
        left, ans = self.rec(root,s)
        return ans