class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for y in range(0,len(nums)):
            
            if(nums[y]!=val):
                k+=1
        for i in range(0,len(nums)):
            #print(nums)
            if(nums[i]==val):
                temp = i
                check = 0
                while(temp<len(nums)):
                    if(nums[temp]!=val and check ==0):
                        x = nums[temp]
                        nums[temp]=nums[i]
                        nums[i]=x
                        check = 1
                    else:
                        temp+=1
        return k
        