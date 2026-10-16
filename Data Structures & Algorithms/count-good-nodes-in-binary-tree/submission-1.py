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
        highest = deque([root.val])
        counter = 1
        while(len(queue)!=0):
            size = len(queue)
            for i in range(0,size):
                ele = queue.pop()
                high = highest.pop()
                if ele.left!=None:
                    if ele.left.val>=high:
                        highest.append(ele.left.val)
                        counter+=1
                    else:
                        highest.append(high)
                    queue.append(ele.left)
                if ele.right!=None:
                    if ele.right.val>=high:
                        highest.append(ele.right.val)
                        counter+=1
                    else:
                        highest.append(high)
                    queue.append(ele.right)
        return counter


        