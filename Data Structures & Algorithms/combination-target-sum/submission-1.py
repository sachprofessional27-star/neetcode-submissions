class Solution:
    def find_sum(self,i,s,nums,target,global_arr,arr):
        if(s==target):
            a=tuple(arr)
            global_arr.add(a)
        if(i>=len(nums)):
            return 
        if(s>target):
            return
        s+=nums[i]
        arr.append(nums[i])
        self.find_sum(i,s,nums,target,global_arr,arr)
        
        s-=nums[i]
        arr.pop()
        self.find_sum(i+1,s,nums,target,global_arr,arr)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        global_arr=set()
        arr = []
        self.find_sum(0,0,nums,target,global_arr,arr)
        ans = []
        for i in global_arr:
            ans.append(list(i))
        return ans
        