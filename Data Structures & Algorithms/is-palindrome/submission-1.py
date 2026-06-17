class Solution:
    def isPalindrome(self, s: str) -> bool:
        #print(ord('A'),ord('Z'),ord('a'),ord('z'),ord('1'),ord('9'))
        k = ''
        for i in range(0,len(s)):
            t = ord(s[i])
            if((t>=65 and t<=90) or (t>=97 and t<=122)):
                k+=s[i].lower()
            elif(t>=48 and t<=57):
                k+=s[i]
        lim = len(k)//2
        ptr = 0
        print(lim,ptr,k)
        while(ptr<lim):

            if(k[ptr]!=k[len(k)-ptr-1]):
                #print(k[ptr],k[len(k)-ptr-1])
                return(False)
            ptr+=1

        return(True)
        