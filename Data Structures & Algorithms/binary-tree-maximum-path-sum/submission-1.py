# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_min_negative(self,root,val):
        if root==None:
            return val
        if root.val>val:
            val = root.val
        return max(self.find_min_negative(root.left,val),self.find_min_negative(root.right,val))
    def find_max_sum(self,root,maxi):
        if(root==None):
            return 0,maxi
        left_max,maxi = self.find_max_sum(root.left,maxi)
        right_max,maxi = self.find_max_sum(root.right,maxi)
        path_value = left_max+right_max+root.val
        maxi = max(path_value,maxi)
        left_path = left_max+root.val
        right_path = right_max+root.val
        if(left_path<0 and right_path<0):
            return 0,maxi
        return max(left_path,right_path),maxi
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_val,maxi = self.find_max_sum(root,0)
        if(maxi==0):
            ans = self.find_min_negative(root,root.val)
            return ans
        return maxi
        