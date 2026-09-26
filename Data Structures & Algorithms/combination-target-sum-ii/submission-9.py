class Solution:
    def p_np(self,i,candidates,arr,s,target,ans):
        if s == target:
            ans.append(arr.copy())
        if i>=len(candidates):
            return
        if s>target:
            return
        
        for j in range(i,len(candidates)):
            if j==i or candidates[j]!=candidates[j-1]:
                s+=candidates[j]
                arr.append(candidates[j])
                self.p_np(j+1,candidates,arr,s,target,ans)
                arr.pop()
                s-=candidates[j]
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol = []
        self.p_np(0,candidates,[],0,target,sol)
        return sol
        