# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self,root,k,ans):
       
        if(k==len(ans) or root==None):
            return
        self.inorder(root.left,k,ans)
        if(len(ans)==k):
            return
        ans.append(root.val)
        self.inorder(root.right,k,ans)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.inorder(root,k,ans)
        print(ans)
        return ans[len(ans)-1]
        