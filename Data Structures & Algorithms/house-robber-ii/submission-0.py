class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        if len(nums)==2:
            return max(nums[1],nums[0])
        if len(nums)==3:
            return max(nums)
        arr1 = [-1]*(len(nums)-1)
        arr2 = [-1]*(len(nums)-1)
        arr1[0] = nums[0]
        arr1[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)-1):
            arr1[i] = max(arr1[i-1],arr1[i-2]+nums[i])
        arr2[0] = nums[1]
        arr2[1] = max(nums[2],nums[1])
        for i in range(3,len(nums)):
            arr2[i-1] = max(arr2[i-2],arr2[i-3]+nums[i])
        print(arr2)
        return max(arr1[-1],arr2[-1])