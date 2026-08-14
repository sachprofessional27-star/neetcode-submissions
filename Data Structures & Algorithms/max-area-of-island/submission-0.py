class Solution:
    def find_area(grid,i,j,area):
        if(i>=len(grid) or j>=len(grid[0])):
            return area
        if(i<0 or j<0):
            return area
        if(grid[i][j]!=1):
            return area
        grid[i][j]=-1
        area+=1
        area = Solution.find_area(grid,i-1,j,area)
        area = Solution.find_area(grid,i+1,j,area)
        area = Solution.find_area(grid,i,j-1,area)
        area = Solution.find_area(grid,i,j+1,area)
        return area
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==1):
                    area = Solution.find_area(grid,i,j,0)
                    if(area>max_area):
                        max_area = area
        return max_area
        