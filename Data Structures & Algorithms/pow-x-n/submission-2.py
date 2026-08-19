class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        try:
            ans = x**abs(n)
        except:
            return float(0)
        if(n>=0):
            return ans
        else:
            return (1/ans)