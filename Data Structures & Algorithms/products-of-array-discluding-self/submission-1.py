class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        z_count = 0
        nz_prod=1
        for i in range(0,len(nums)):
            if(nums[i]==0 and z_count==0):
                prod=0
                z_count+=1
            elif(nums[i]==0 and z_count==1):
                ans=[]
                for j in range(len(nums)):
                    ans.append(0)
                return(ans)
            else:
                nz_prod=nz_prod*nums[i]
                prod = prod*nums[i]
        ans = []
        
        for j in range(0,len(nums)):
            if(nums[j]==0):
                
                ans.append(nz_prod)
            else:
                ans.append(prod//nums[j])
        return(ans)
        