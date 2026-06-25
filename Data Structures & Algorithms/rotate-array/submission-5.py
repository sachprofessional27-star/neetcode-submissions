class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        post = []
        pre = []
        k = k%len(nums)
        n = len(nums)
        for i in range(n-k,n):
            post.append(nums[i])
        for j in range(0,n-k):
            pre.append(nums[j])
        for x in range(0,len(post)):
            nums[x]=post[x]
        for z in range(0,len(pre)):
            nums[z+k]=pre[z]