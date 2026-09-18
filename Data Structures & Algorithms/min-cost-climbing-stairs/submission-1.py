class Solution:
    def mem(self,s,cost,dp):
        if(s==len(cost)-2):
            dp[len(dp)-2] = cost[len(cost)-2]
            return cost[len(cost)-2]
        if s==len(cost)-1:
            dp[len(dp)-1] = cost[len(cost)-1]
            return cost[len(cost)-1]
        if dp[s]!=-1:
            return dp[s]
        one_step = self.mem(s+1,cost,dp)
        two_step = self.mem(s+2,cost,dp)
        dp[s]=min(one_step,two_step)+cost[s]
        return dp[s]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2:
            return min(cost)
        dp = [-1]*len(cost)
        self.mem(0,cost,dp)
        return min(dp[0],dp[1])        