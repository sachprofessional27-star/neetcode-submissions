class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        count = 0
        start = -1000000000000
        for i in range(0,len(nums)):
            if(nums[i]==start):
                pass
            elif(nums[i]==start+1):
                count+=1
                start = nums[i]
            else:
                start = nums[i]
                count=1
            if(count>maxi):
                maxi=count     
        return(maxi)