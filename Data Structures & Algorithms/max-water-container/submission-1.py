class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left =0
        right = len(heights)-1
        maxi = 0
        while(left<right):
            if(heights[left]<heights[right]):
                area = heights[left]*(right-left)
                if(area>maxi):
                    maxi=area
                left+=1
            else:
                area = heights[right]*(right-left)
                if(area>maxi):
                    maxi=area
                right-=1
        return maxi


