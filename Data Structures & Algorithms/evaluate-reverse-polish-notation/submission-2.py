class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(0,len(tokens)):
           # print(stk)
            if(tokens[i]=='+' or tokens[i]=='-' or tokens[i]=='*' or tokens[i]=='/'):
                if(tokens[i]=='+'):
                    a = stk.pop(len(stk)-2)
                    b = stk.pop(len(stk)-1)
                    c = a+b
                    stk.append(c)
                elif(tokens[i]=='-'):
                    a = stk.pop(len(stk)-2)
                    b = stk.pop(len(stk)-1)
                    c = a-b
                    stk.append(c)
                elif(tokens[i]=='*'):
                    a = stk.pop(len(stk)-2)
                    b = stk.pop(len(stk)-1)
                    c = a*b
                    stk.append(c)
                elif(tokens[i]=='/'):
                    a = stk.pop(len(stk)-2)
                    b = stk.pop(len(stk)-1)
                    c = int(a/b)
                    stk.append(c)
            else:
                stk.append(int(tokens[i]))
        return(stk[0])