from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=defaultdict(int)
        for i in range(0,len(nums)):
            if(nums[i] in dic.keys()):
                
                return([dic[nums[i]],i])
            else:
                key = target-nums[i]
                dic[key]=i
            

            
        