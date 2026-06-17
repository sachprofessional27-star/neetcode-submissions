class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        largest = 0
        i = 0
        while(i<len(s)):
            j=i
            temp = 0
            check = set()
            while(j<len(s)):
                prior = len(check)
                check.add(s[j])
                post = len(check)
                if(prior!=post):
                    if(largest<j-i+1):
                        #print(j,i,s[j],s[i])
                        
                        largest=(j-i)+1
                    
                else:
                    break
                j+=1
            i+=1
        return(largest)

        