class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while(left<=right):
            print(left,mid,right)
            if(nums[mid]==target):
                return mid
            else:
                if(nums[mid]<=nums[right]):
                    if(target>nums[mid] and target<=nums[right]):
                        if(target==nums[right]):
                            return right
                        else:
                            left=mid+1
                    else:
                        right = mid -1
                else:
                    
                    if(nums[mid]>target and nums[left]<=target):
                        
                        if(target==nums[left]):
                            return left
                        else:
                            right = mid -1
                    else:
                        left = mid+1
                mid = (left+right)//2
        return -1
