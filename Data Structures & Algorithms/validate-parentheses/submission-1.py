class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in range(0,len(s)):
            top = len(stk)-1
            if(s[i]=='(' or s[i]=='[' or s[i]=='{'):
                stk.append(s[i])

            elif(s[i]==')'):
                if(top<0):
                    return False
                if(stk[top]=='('):
                    stk.pop(len(stk)-1)
                else:
                    return(False)
            elif(s[i]==']'):
                if(top<0):
                    return False
                if(stk[top]=='['):
                    stk.pop(top)
                else:
                    return(False)
            else:
                if(top<0):
                    return False
                if(stk[top]=='{'):
                    stk.pop(top)
                else:
                    return(False)
        if(len(stk)==0):
            return(True)
        else:
            return(False)