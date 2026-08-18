class Solution:
    def gen_all(self,i,nums,arr,global_set):
        if(i==len(nums)):
            arr1=tuple(arr)
            global_set.add(arr1)
            return
        self.gen_all(i+1,nums,arr,global_set)
        arr.append(nums[i])
        self.gen_all(i+1,nums,arr,global_set)
        arr.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        global_set = set()
        nums.sort()
        self.gen_all(0,nums,[],global_set)
        return(list(global_set))
        