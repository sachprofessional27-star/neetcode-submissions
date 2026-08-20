class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits)==0):
            return []
        dic = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }
        arr = []
        
        for i in range(0,len(digits)):
            
            x = digits[i]
            for k in dic:
                if(k==x):
                    arr.append(dic[k])
                    break
            
        ptr = [0]*len(arr)
        ans = []
        
        while(True):
            
            s = ""
            for j in range(0,len(arr)):
                s+=str(arr[j][ptr[j]])
            ans.append(s)
            out = False
            for j in range(len(ptr)-1,-1,-1):
                if(j==0):
                    ptr[0]+=1
                    if(ptr[0]>=len(arr[0])):
                        out = True
                        break
                else:
                    ptr[j]+=1
                    if(ptr[j]>=len(arr[j])):
                        ptr[j]=0
                    else:
                        break
            if(out==True):
                break
        return ans


            