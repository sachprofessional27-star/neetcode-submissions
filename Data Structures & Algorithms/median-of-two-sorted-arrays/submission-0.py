class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        ptr1,ptr2 = 0,0
        while(ptr1<len(nums1) and ptr2<len(nums2)):
            if(nums1[ptr1]<nums2[ptr2]):
                arr.append(nums1[ptr1])
                ptr1+=1
            else:
                arr.append(nums2[ptr2])
                ptr2+=1
        while(ptr1<len(nums1)):
            arr.append(nums1[ptr1])
            ptr1+=1
        while(ptr2<len(nums2)):
            arr.append(nums2[ptr2])
            ptr2+=1
        if(len(arr)%2==0):
            ans1,ans2 = arr[len(arr)//2],arr[(len(arr)//2)-1]
            return((ans1+ans2)/2)
        else:
            return arr[len(arr)//2]
        