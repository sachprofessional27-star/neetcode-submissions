class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[]
        maxi_l=height[0]
        max_left.append(0)
        for i in range(1,len(height)):
            max_left.append(maxi_l)
            if(height[i]>maxi_l):
                maxi_l=height[i]
        max_right = []
        maxi_r = height[len(height)-1]
        max_right.append(0)
        for j in range(len(height)-2,-1,-1):
            max_right.append(maxi_r)
            if(height[j]>maxi_r):
                maxi_r = height[j]
        s = 0
        max_right = max_right[::-1]
        #print(max_left,max_right)
        for k in range(0,len(max_right)):
            t = min(max_right[k],max_left[k])-height[k]
            if(t>0):
                s=s+min(max_right[k],max_left[k])-height[k]
            else:
                pass
        return(s)
        