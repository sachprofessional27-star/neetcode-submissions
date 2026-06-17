class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 100000000
        maxi = 0 
        ans = 0
        for i in range(0,len(prices)):
            if(prices[i]>maxi):
                maxi = prices[i]
            if(prices[i]<mini):
                mini = prices[i]
                maxi = prices[i]
            prof = maxi-mini
            if(prof>ans):
                ans= prof
        return(ans)
        