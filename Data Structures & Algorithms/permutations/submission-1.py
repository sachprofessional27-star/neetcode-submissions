class Solution:
    def perm(self,marked,nums,ans,arr,i):
       
        if i==len(nums):
            ans.append(arr.copy())
            return 
        if i>len(nums):
            return
        
        for j in range(0,len(nums)):
            if marked[j]!=1:
              
                marked[j]=1
                arr.append(nums[j])
                self.perm(marked,nums,ans,arr,i+1)
                marked[j]=-1
                arr.pop()
        
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        marked = []
        for i in range(0,len(nums)):
            marked.append(-1)
        self.perm(marked,nums,ans,[],0)
        return ans