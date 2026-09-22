class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = []
        for i in range(0,len(nums)+1):
            freq.append([])
        for i in range(0,len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        for i in dic:
            print(dic[i])
            freq[dic[i]].append(i)
        ans = []
        i = len(freq)-1
      
        while(k>0):
            if len(freq[i])>0:
                for j in range(0,len(freq[i])):
                    ans.append(freq[i][j])
                    k-=1
            i-=1
        return ans
        