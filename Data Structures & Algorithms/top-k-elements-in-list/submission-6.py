class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(0,len(nums)):
            if(nums[i] in count):
                count[nums[i]]+=1
            else:
                count[nums[i]]=1 

        arr = [[]]*(len(nums)+1)
        # print(count)
        for j in count:
            
            if(len(arr[count[j]])>=1):
                arr[count[j]].append(j)
            else:
                arr[count[j]]=[j]
            print(arr)
        ans = []
        ptr = len(arr)-1
        while(k>0):   
            for x in range(0,len(arr[ptr])):
                if(k>0):
                    ans.append(arr[ptr][x])
                    k-=1
                else:
                    break
            ptr-=1
        
        return ans    
