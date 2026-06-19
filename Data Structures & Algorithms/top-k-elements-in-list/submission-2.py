class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(0,len(nums)):
            if(nums[i] in counts):
                counts[nums[i]]+=1
            else:
                counts[nums[i]]=1
        frequents = []
        for j in range(0,k):
            maxi = 0
            key_maxi = -1
            for l in counts:
                if(counts[l]>maxi):
                    maxi = counts[l]
                    key_maxi= l
            frequents.append(key_maxi)
            counts[key_maxi] = -1
        return frequents
                
        