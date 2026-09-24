class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set()
        for i in range(0,len(nums)):
            a.add(nums[i])
        starters = []
        for i in range(0,len(nums)):
            if nums[i] in a and nums[i]-1 not in a:
                starters.append(nums[i])
        maxi = 0
        for i in range(0,len(starters)):
            ele = starters[i]
            counter = 0
            while True:
                if ele in a:
                    counter+=1
                    ele+=1
                else:
                    break
            maxi = max(counter,maxi)
        return maxi       
        