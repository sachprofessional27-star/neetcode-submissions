class Solution:
    def gen_subsets(self,nums,i,arr,global_arr):
        if(i==len(nums)):
            global_arr.append(arr.copy())
            return global_arr
        
        global_arr = self.gen_subsets(nums,i+1,arr,global_arr)
        arr.append(nums[i])
        global_arr = self.gen_subsets(nums,i+1,arr,global_arr)
        arr.pop()
        return global_arr

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = self.gen_subsets(nums,0,[],[])
        return ans