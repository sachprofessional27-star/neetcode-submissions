from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k = Counter(s)
        q = Counter(t)
        return(k==q)
            
        