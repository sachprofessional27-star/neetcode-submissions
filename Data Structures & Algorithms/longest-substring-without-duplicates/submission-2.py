class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        ans = 0
        r=0
        l=0
        while(r<len(s)):
            prior = len(x)
            x.add(s[r])
            post = len(x)
            if(prior==post):
                x.remove(s[l])
                l+=1
            else:
                r+=1
            if(len(x)>ans):
                ans= len(x)
        return(ans)
            
        