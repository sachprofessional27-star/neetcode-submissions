class Solution:
    def rec(self,arr,nums,ans_arr,marked):
        
        if(len(arr)==len(nums)):
            ans_arr.append(arr.copy())
            return 
        # if(idx>=len(nums)):
        #     return 
        for i in range(0,len(nums)):
            if(marked[i]==0):
                arr.append(nums[i])
                marked[i]=1
                self.rec(arr,nums,ans_arr,marked)
                arr.pop()
                marked[i]=0
        
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans_arr = []
        marked = [0]*len(nums)
        self.rec([],nums,ans_arr,marked)
        return ans_arr
        