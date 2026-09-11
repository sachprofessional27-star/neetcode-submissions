# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def find_dia(self,root,dia):
        if root is None:
            return 0,dia
        left,dia = self.find_dia(root.left,dia)
        right,dia = self.find_dia(root.right,dia)
        if left+right>dia:
            dia = left+right
        return max(left+1,right+1),dia
    def diameterOfBinaryTree(self, root):
        #your code goes here
        r,dia = self.find_dia(root,0)
        return dia