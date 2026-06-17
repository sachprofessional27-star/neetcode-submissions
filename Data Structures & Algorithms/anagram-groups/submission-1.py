class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_array = []
        groups = []
        for i in range(0,len(strs)):
            temp={}
            for j in range(0,len(strs[i])):
                if(strs[i][j] in temp):
                    temp[strs[i][j]]+=1
                else:
                    temp[strs[i][j]]=1
            flag = True
            for k in range(0,len(dict_array)):
                # print(len(dict_array[k]),len(temp))
                if(len(dict_array[k])!=len(temp)):
                    pass
                else:
                    is_equal = True
                    for x in dict_array[k]:
                        if(x not in temp):
                            is_equal = False
                            break
                        if(dict_array[k][x]!=temp[x]):
                            is_equal = False
                            break

                    if(is_equal):
                        groups[k].append(strs[i])
                        flag = False
            if(flag):
                dict_array.append(temp)
                groups.append([strs[i]])
        return groups