class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictonary = {}
        for i in range(0,len(strs)):
            temp = [0]*26
            for j in range(0,len(strs[i])):
                temp[ord(strs[i][j])-ord('a')]+=1
            temp_1 = tuple(temp)
            if temp_1 in dictonary:
                dictonary[temp_1].append(strs[i])
            else:
                dictonary[temp_1]=[strs[i]]
        out = []
        for k in dictonary:
            t = dictonary[k]
            out.append(t)
        return out
        