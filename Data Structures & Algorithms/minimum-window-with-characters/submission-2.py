class Solution:
    def is_substring(self,freq,compare_freq):
        for i in freq:
            if(i not in compare_freq):
                return False
            elif(freq[i]>compare_freq[i]):
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        if(len(t)>len(s)):
            return ""
        if(t==s):
            return t
        freq = {}
        for i in t:
            if(i in freq):
                freq[i]+=1
            else:
                freq[i]=1
        left = 0
        right = 0
        string_exists = False
        compare_freq = {}
        min_length = 10**9
        min_left = -1
        min_right = -1
        while(right<len(s)):
            # print(s[left],left,s[right],right)
            while(right<len(s)):
                if(s[right] in compare_freq):
                    compare_freq[s[right]]+=1
                else:
                    compare_freq[s[right]]=1
                if(self.is_substring(freq,compare_freq)):
                    string_exists = True
                    
                    # print(freq,compare_freq,right)
                    break
                right+=1
            
            while(left<=right):
                compare_freq[s[left]]-=1
                if(self.is_substring(freq,compare_freq)):
                    left+=1
                else:
                    if(len(s[left:right+1])<min_length):
                        min_length = len(s[left:right+1])
                        min_left = left
                        min_right = right
                        # print(min_left,min_right,min_length)
                    compare_freq[s[left]]+=1
                    
                    break
            right+=1
        if(string_exists==False):
            print('here')
            return ""
        while(True):
            compare_freq[s[min_right]]-=1
            if(self.is_substring(freq,compare_freq)):
                min_right-=1
            else:
                break
        return(s[min_left:min_right+1])
            

        