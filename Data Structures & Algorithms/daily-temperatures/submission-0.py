class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = []
        for i in range(0,len(temperatures)):
            ans.append(0)
        for j in range(0,len(temperatures)):
            if(len(stk)>0):
                while(True):
                    if(stk[-1][0]<temperatures[j]):
                        val,idx = stk.pop()
                        ans[idx]=j-idx
                        if(len(stk)==0):
                            stk.append([temperatures[j],j])
                            break
                    else:
                        stk.append([temperatures[j],j])
                        break

            else:
                stk.append([temperatures[j],j])
        return(ans)