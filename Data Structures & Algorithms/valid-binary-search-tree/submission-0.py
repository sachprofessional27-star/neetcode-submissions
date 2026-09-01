# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validate(self,root,arr):
        if root is None:
            return 
        self.validate(root.left,arr)
        arr.append(root.val)
        self.validate(root.right,arr)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        self.validate(root,ans)
        for i in range(0,len(ans)-1):
            if ans[i]>=ans[i+1]:
                return False
        return True 