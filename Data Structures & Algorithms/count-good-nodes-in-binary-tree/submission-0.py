# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([root])
        max_queue = deque([root.val])
        good_nodes = 0
        while(len(queue)>0):
            size = len(queue)
            for i in range(0,size):
                element = queue.popleft()
                maxi = max_queue.popleft()
                if(element.val>=maxi):
                    good_nodes+=1
                    maxi = element.val
                if element.left is not None:
                    queue.append(element.left)
                    max_queue.append(maxi)
                if element.right is not None:
                    queue.append(element.right)
                    max_queue.append(maxi)
        return good_nodes
                
                

        