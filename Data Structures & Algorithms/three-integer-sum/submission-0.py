class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        import copy
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(0,len(nums)):
            target = 0-nums[i]
            left = 0
            right = len(nums)-1
            #print(target,nums)
            while(left<right):
                if(left == i):
                    left+=1
                elif(right == i):
                    right=right-1
                else:
                    k = nums[left]+nums[right]
                    if(k==target):
                        p = [nums[i],nums[left],nums[right]]
                        
                        
                        ans.add(tuple(sorted(p)))
                        
                        while(left<right and nums[left]==nums[left+1]):
                            left+=1
                        while(left<right and nums[right]==nums[right-1]):
                            right-=1

                        left+=1
                        right-=1
                    elif(k>target):
                        right-=1
                    else:
                        left+=1
        ans1 = []
        for i in ans:
            ans1.append(list(i))
        return(ans1)
                
        
        