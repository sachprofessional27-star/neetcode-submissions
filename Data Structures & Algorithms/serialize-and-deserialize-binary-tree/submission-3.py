# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    # Encodes a tree to a single string.
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        print("here")
        if root is None:
            return ""
        queue = deque([root])
        ans.append([root.val])
        while(len(queue)>0):
            size = len(queue)
            temp =[]
            for i in range(0,size):
                element = queue.popleft()
                if element is None:
                    continue
                
                if element.left is not None:
                    temp.append(element.left.val)
                    queue.append(element.left)
                else:
                    temp.append("null")
                if element.right is not None:
                    temp.append(element.right.val)
                    queue.append(element.right)
                else:
                    temp.append("null")
            
            ans.append(temp)
        s = []
       
        for i in range(0,len(ans)-1):
            arr = ans[i]
            for j in range(0,len(arr)):
                s.append(str(arr[j]))
        
        ptr = len(s)-1
        while(True):
            if(s[ptr]!='null'):
                break
            ptr-=1
        k = ""
        s = s[:ptr+1:]
        for i in range(0,len(s)):
            k += s[i]
            if i==len(s)-1:
                continue
            k+=" "        
        return k
 
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = data.split()
        print(lst)
        if len(data)==0:
            return None
        
        root = TreeNode(lst[0])
        queue = deque([root])
        power = 0
        ptr = 1
        while ptr<len(lst):
            itr = 2**power
            # print(itr)
            for i in range(0,itr):
                if(ptr==len(lst)):
                    break
                # print(queue)
                element = queue.popleft()
                if element == "null":
                    continue
                node_left = TreeNode(lst[ptr])
                element.left = node_left
                queue.append(element.left)
                ptr+=1
                if(ptr==len(lst)):
                    break
                node_right = TreeNode(lst[ptr])
                element.right = node_right
                queue.append(element.right)
                ptr+=1
            power+=1
        return root
