class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(0,len(strs)):
            arr = [0]*26
            for j in range(0,len(strs[i])):
                arr[ord(strs[i][j])-ord('a')]+=1
            arr = tuple(arr)
            if arr not in dic:
                dic[arr] = [strs[i]]
            else:
                dic[arr].append(strs[i])
        ans = []
        for i in dic:
            ans.append(dic[i])
        return ans
        