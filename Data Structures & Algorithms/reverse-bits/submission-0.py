class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = ""
        while(n>0):
            if(n%2==0):
                binary_str +="0"
            else:
                binary_str +="1"
            n=n//2
        zero_string = ""
        for i in range(0,32-len(binary_str)):
            zero_string +="0"
        reverse_string = binary_str+zero_string
        print(reverse_string)
        power = 0
        ans = 0
        for i in range(len(reverse_string)-1,-1,-1):
            if(reverse_string[i]=="1"):
                ans+=2**power
            power+=1
        return ans
        