import math
class Solution:
    def satisfies(self,piles,k,h):
        time = 0
        for i in range(0,len(piles)):
            time = time+math.ceil(piles[i]/k)
        return(time<=h)
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        lower_bound = 1
        mid = math.ceil((upper_bound+lower_bound)/2)
        while(mid<upper_bound):
            if(self.satisfies(piles,mid,h)):
                upper_bound=mid
                mid = math.ceil((lower_bound+upper_bound)/2)
            else:
                lower_bound = mid
                mid = math.ceil((lower_bound+upper_bound)/2)
        if(self.satisfies(piles,mid-1,h)):
            return mid-1
        return mid
