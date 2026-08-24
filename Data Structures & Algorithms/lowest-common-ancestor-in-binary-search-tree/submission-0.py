# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_path(self,node,arr,target,nodes):
        if(node==None):
            return
        arr.append(node.val)
        nodes.append(node)
        if(node.val==target):
            return
        if(node.val>target):
            self.find_path(node.left,arr,target,nodes)
        if(node.val<target):
            self.find_path(node.right,arr,target,nodes)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        arr1 = []
        arr2 = []
        n1 = []
        n2 = []
        self.find_path(root,arr1,p.val,n1)
        self.find_path(root,arr2,q.val,n2)
        x = set(arr1)
        for i in range(len(arr2)-1,-1,-1):
            if(arr2[i] in x):
                return n2[i]
        