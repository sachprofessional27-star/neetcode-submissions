class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = set()
        for i in range(0,len(nums)):
            target = nums[i]*(-1)
            left = 0
            right = len(nums)-1
            while(left<right):
                if(left==i):
                    left+=1
                    continue 
                if(right==i):
                    right-=1
                    continue
                temp = nums[left]+nums[right]
                if(temp==target):
                    temp_list = [nums[left],nums[right],nums[i]]
                    temp_list.sort()
                    temp_tup = tuple(temp_list)
                    lst.add(temp_tup)
                    left+=1
                    # break
                elif(temp<target):
                    left+=1
                else:
                    right-=1
        triplets = []
        for k in lst:
            triplets.append(list(k))
        return triplets

            
        