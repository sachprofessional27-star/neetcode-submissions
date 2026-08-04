class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_length = 0
        freq_arr = [0]*26
        base = ord("A")
        max_freq = 0
        while(right<len(s)):
            freq_arr[ord(s[right])-base]+=1
            max_freq = max(max_freq,freq_arr[ord(s[right])-base])
            window = right-left+1
            while(window-max_freq>k):
                freq_arr[ord(s[left])-base]-=1
                left+=1
                window = right-left+1
                max_freq = max(freq_arr)
            if(window-max_freq<=k):
                max_length = max(max_length,window)
            right+=1
            
        return max_length



            