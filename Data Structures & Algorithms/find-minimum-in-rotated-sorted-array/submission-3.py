class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums)-1
        left = 0
        mid = (left+right)//2
        temp_min = nums[mid]
        while(left<=right):
            
            if(nums[mid]<temp_min):
                temp_min = nums[mid]
            if(nums[mid]<=nums[right]):
                right = mid -1
            else:
                left = mid+1
            mid = (left+right)//2
                
                
        return temp_min