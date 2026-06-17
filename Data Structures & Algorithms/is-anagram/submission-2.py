class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for i in range(0,len(s)):
            if(s[i] in dic1):
                dic1[s[i]]+=1
            else:
                dic1[s[i]]=1
        for j in range(0,len(t)):
            if(t[j] in dic2):
                dic2[t[j]]+=1
            else:
                dic2[t[j]]=1
        
        if(len(dic1)!=len(dic2)):
            return(False)
        else:
            for k in dic1:
                if(k not in dic2):
                    return False
                else:
                    if(dic1[k]!=dic2[k]):
                        return False
            return True
        