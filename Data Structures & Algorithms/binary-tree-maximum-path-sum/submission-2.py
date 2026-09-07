# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_max(self,root,maxi):
        if root is None:
            return 0,maxi
        left,maxi = self.find_max(root.left,maxi)
        right,maxi = self.find_max(root.right,maxi)
        path = left+right+root.val
        if(path>maxi):
            maxi = path
        path_left = left+root.val
        path_right = right+root.val
        if(path_left<0 and path_right<0):
            return 0,maxi
        return max(path_left,path_right),maxi
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path, maxi = self.find_max(root,float('-inf'))
        return maxi