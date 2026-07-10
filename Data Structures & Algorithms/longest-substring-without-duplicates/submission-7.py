class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        maxi = 0
        left = 0
        right = 0
        while(right<len(s)):
            prior = len(check)
            check.add(s[right])
            post = len(check)
            if(prior!=post):
                if(maxi<len(check)):
                    maxi = len(check)
            else:
                while(True):
                    check.remove(s[left])
                    prior = len(check)
                    check.add(s[right])
                    post = len(check)
                    left+=1
                    if(prior!=post):
                        break
            right+=1
        return maxi

            
        