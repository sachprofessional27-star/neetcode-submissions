# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        level_order = []
        while(len(queue)>0):
            temp = []
            size = len(queue)
            for i in range(0,size):
                element = queue.popleft()
                temp.append(element.val)
                if(element.left!=None):
                    queue.append(element.left)
                if(element.right!=None):
                    queue.append(element.right)
            level_order.append(temp)
        right_view = []
        for i in range(0,len(level_order)):
            arr = level_order[i]
            element = arr[-1]
            right_view.append(element)
        return right_view