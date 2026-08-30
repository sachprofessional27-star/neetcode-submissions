# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_depth(self,root,dia):
        
        if(root==None):
            return 0,dia
        left,dia = self.find_depth(root.left,dia)
        right,dia = self.find_depth(root.right,dia)
       
        
        if(left+right>dia):
            
            dia = left+right
        return 1+max(left,right),dia

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter,dia = self.find_depth(root,0)
        return dia