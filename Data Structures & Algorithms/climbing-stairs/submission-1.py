class Solution:
    def rec(self,n,s,dp):
        
        if(dp[s]!=-1):
           
            return dp[s]
        if(s==n-1):
            dp[n-1]=1
            return 1
        if(s==n-2):
            dp[n-2]=2
            return 2
        dp[s]=self.rec(n,s+1,dp)+self.rec(n,s+2,dp)
        return dp[s]
    def climbStairs(self, n: int) -> int:
        dp = [-1]*n
        self.rec(n,0,dp)
        return dp[0]
        