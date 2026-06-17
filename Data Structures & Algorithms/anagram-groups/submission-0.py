from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in range(0,len(strs)):
            k = sorted(strs[i])
            k=''.join(k)
            dic[k].append(strs[i])
        ans = []
        for val in dic.keys():
            ans.append(dic[val])

        return(ans)
        