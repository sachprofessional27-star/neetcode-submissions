class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in range(0,len(nums)):
            prior = len(a)
            a.add(nums[i])
            post = len(a)
            if(prior==post):
                return True
        return False
        