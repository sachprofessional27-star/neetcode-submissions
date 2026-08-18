class Solution:
    def find_sum(self,i,s,nums,target,global_arr,arr):
        if(s>target):
            return
        if(s==target):
           
            global_arr.append(arr.copy())
            return
        if(i>=len(nums)):
            return 
        if(s>target):
            return
        
        for j in range(i,len(nums)):
            if(j!=i and nums[j]==nums[j-1]):
                continue
            else:
                s+=nums[j]
                arr.append(nums[j])
                self.find_sum(j+1,s,nums,target,global_arr,arr)
                s-=nums[j]
                arr.pop()
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        global_arr=[]
        arr = []
        nums.sort()
        self.find_sum(0,0,nums,target,global_arr,arr)
        
        return global_arr
        