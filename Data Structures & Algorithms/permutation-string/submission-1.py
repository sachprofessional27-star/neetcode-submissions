class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        if(len(s1)>len(s2)):
            return False
        if(s1==s2):
            return True
        for i in range(0,len(s1)):
            if(s1[i] in dic):
                dic[s1[i]]+=1
            else:
                dic[s1[i]]=1
        
        compare_dic = {}
        for j in dic:
            compare_dic[j]=0
        window_start = 0
        window_end = len(s1)-1
        for i in range(0,len(s1)):
            if(s2[i] in compare_dic):
                compare_dic[s2[i]]+=1
        window_start+=1
        window_end+=1
        if(dic==compare_dic):
            return True
        while(window_end<len(s2)):
            if(s2[window_start-1] in compare_dic):
                compare_dic[s2[window_start-1]]-=1
            if(s2[window_end] in compare_dic):
                compare_dic[s2[window_end]]+=1
            if(compare_dic == dic):
                return True
            window_start+=1
            window_end+=1
        return False
        