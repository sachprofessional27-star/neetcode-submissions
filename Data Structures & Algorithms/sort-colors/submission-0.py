class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_count = 0
        white_count = 0
        blue_count = 0
        for i in range(0,len(nums)):
            if(nums[i]==0):
                red_count+=1
            elif(nums[i]==1):
                white_count+=1
            else:
                blue_count+=1
        for k in range(0,red_count):
            nums[k]=0
        for k in range(red_count,white_count+red_count):
            nums[k]=1
        for k in range(white_count+red_count,blue_count+white_count+red_count):
            nums[k]=2
        
        