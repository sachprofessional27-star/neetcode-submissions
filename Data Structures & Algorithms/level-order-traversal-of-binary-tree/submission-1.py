# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):
            return []
        
        queue = deque([root])
        ans = []
       
        temp = []
        while(len(queue)!=0):
           
            temp = []
            while(len(queue)!=0):
                temp.append(queue.popleft())
            for i in range(0,len(temp)):
                if(temp[i].left!=None):
                    queue.append(temp[i].left)
                if(temp[i].right!=None):
                    queue.append(temp[i].right)
            for j in range(0,len(temp)):
                temp[j]=temp[j].val
            ans.append(temp)
        return ans
            