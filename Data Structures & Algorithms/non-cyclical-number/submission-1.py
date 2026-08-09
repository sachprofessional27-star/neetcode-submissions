class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        s = n
        while(True):
            temp = s
            s = 0
            while(temp>0):
                x = temp%10
                
                s+=x**2
                temp=temp//10
         
            if(s==1):
                return True
            else:
                if(s in visited):
                    return False
                else:
                    visited.add(s)


        