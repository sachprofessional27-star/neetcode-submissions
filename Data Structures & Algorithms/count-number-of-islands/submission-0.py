class Solution:
    def mark_islands(self,grid,row,col):
        if(row<0 or col<0):
            return
        if(row>=len(grid) or col>=len(grid[0])):
            return
        if(grid[row][col]=="0" or grid[row][col]=="-1"):
            return
        if(grid[row][col]=="1"):
            grid[row][col]="-1"
        self.mark_islands(grid,row+1,col)
        self.mark_islands(grid,row-1,col)
        self.mark_islands(grid,row,col+1)
        self.mark_islands(grid,row,col-1)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if(grid[i][j]=="1"):
                    count+=1
                    self.mark_islands(grid,i,j)
        return count