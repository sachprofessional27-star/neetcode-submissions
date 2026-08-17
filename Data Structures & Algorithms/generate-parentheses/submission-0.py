class Solution:
    def is_valid(self,arr):
        
        stk = []
        for i in range(0,len(arr)):
            if(arr[i]=='('):
                stk.append('(')
            if(arr[i]==')'):
                if(len(stk)==0):
                    return False
                if(stk[-1]!='('):
                    return False
                else:
                    stk.pop()
        return(len(stk)==0)
    def generate(self,m,i,arr,global_arr):
        # print(m,i)
        if(m==len(arr)):
            if(self.is_valid(arr)):
                s=""
                for i in range(0,len(arr)):
                    s+=arr[i]
                global_arr.append(s)
            return
        if(m<i):
            return
        arr.append('(')
        self.generate(m,i+1,arr,global_arr)
        arr.pop()
        arr.append(')')
        self.generate(m,i+1,arr,global_arr)
        arr.pop()
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        global_arr = []
        arr = []
        self.generate(n*2,0,arr,global_arr)
        
        return global_arr
        