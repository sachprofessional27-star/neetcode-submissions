class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_counter=0
        prod_w_z = 1
        for i in range(0,len(nums)):
            if(nums[i]==0):
                zero_counter+=1
            else:
                prod_w_z=prod_w_z*nums[i]
            prod = prod*nums[i]
        if(zero_counter>=2):
            return([0]*len(nums))
        ans = []
        for j in range(0,len(nums)):
            if(nums[j]==0):
                ans.append(prod_w_z)
            else:
                temp = int(prod/nums[j])
                ans.append(temp)
        return ans