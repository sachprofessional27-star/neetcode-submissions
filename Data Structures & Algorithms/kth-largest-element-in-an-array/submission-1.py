class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = [0]*2001
        for i in range(0,len(nums)):
            ans[nums[i]+1000]+=1
        for j in range(len(ans)-1,-1,-1):
            k=k-ans[j]
            if(k<=0):
                return(j-1000)

        