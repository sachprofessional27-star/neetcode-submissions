class Solution:
    def gen_all(self,i,nums,arr,global_arr):
        if(i>len(nums)):
            return
            
        global_arr.append(arr.copy())
            
        for idx in range(i,len(nums)):
            if(idx!=i and nums[idx]==nums[idx-1]):
                continue
            else:
                arr.append(nums[idx])
                # print(arr)
                self.gen_all(idx+1,nums,arr,global_arr)
                arr.pop()

        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        global_arr = []
        nums.sort()
        self.gen_all(0,nums,[],global_arr)
        return(global_arr)
        