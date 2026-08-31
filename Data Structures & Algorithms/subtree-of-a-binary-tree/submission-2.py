# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def are_equal(self,root,subRoot,searching):
        if(root == None and subRoot==None):
            return True
        if((root!=None and subRoot==None) or (root==None and subRoot!=None)):
            return False
        if(root.val!=subRoot.val):
            if(searching):
                return self.are_equal(root.left,subRoot,True) or self.are_equal(root.right,subRoot,True)
        else:
            left = self.are_equal(root.left,subRoot.left,False)
            right = self.are_equal(root.right,subRoot.right,False)
            if(left==True and right==True):
                return True
            return self.are_equal(root.left,subRoot,True) or self.are_equal(root.right,subRoot,True)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        node = None
        
        ans = self.are_equal(root,subRoot,True)
        return ans
        