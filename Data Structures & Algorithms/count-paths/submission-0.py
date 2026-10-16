class Solution:
    def rec(self,r,c,m,n,dp):
        if r>=m or c>=n:
            return
        if r<0 or c<0:
            return
        if r==0 and c==0:
            return 
 
        
        if r==m-1 and c==n-1:
            self.rec(r-1,c,m,n,dp)
            self.rec(r,c-1,m,n,dp)
        else:
            if dp[r][c]!=-1:
                
                return
            ans = 0
            if r+1<=m-1:
                if dp[r+1][c]!=-1:
                    ans+=dp[r+1][c]
                else:
                    return
            if c+1<=n-1:
                if dp[r][c+1]!=-1:
                    ans+=dp[r][c+1]
                else:
                    return
           
            dp[r][c]=ans
            self.rec(r-1,c,m,n,dp)
            self.rec(r,c-1,m,n,dp)


        
    def uniquePaths(self, m, n):
        dp = []
        if m<2 or n<2:
            return 1
        for i in range(0,m):
            arr = []
            for j in range(0,n):
                arr.append(-1)
            dp.append(arr)
        dp[m-1][n-1]=1
        self.rec(m-1,n-1,m,n,dp)

        return dp[0][1]+dp[1][0]