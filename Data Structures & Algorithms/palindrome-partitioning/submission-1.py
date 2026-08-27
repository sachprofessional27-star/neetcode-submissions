class Solution:
    def is_pal(self,st):
        
        left = 0
        right = len(st)-1
        while(left<right):
            if(st[left]!=st[right]):
                return False
            left+=1
            right-=1
        return True
    
            
    def gen_valid_partitions(self,s,index,arr,answer):
        if(index==len(s)):
           
            answer.append(arr.copy())
            return
        for i in range(index,len(s)):
            sub_str = s[index:i+1]
            if(self.is_pal(sub_str)):
                arr.append(sub_str)
                self.gen_valid_partitions(s,i+1,arr,answer)
                arr.pop()

    def partition(self, s: str) -> List[List[str]]:
        arr = []
        answer = []
        print(answer)
        self.gen_valid_partitions(s,0,arr,answer)
        return answer

        