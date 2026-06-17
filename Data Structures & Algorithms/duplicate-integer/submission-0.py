class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for i in range(0,len(nums)):
            a.add(nums[i])
        return(not(len(a)==len(nums)))
         