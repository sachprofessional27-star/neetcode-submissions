class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        top = 0
        bottom = len(matrix)-1
        mid = (top+bottom)//2
        while(top<=bottom):
            print(mid,bottom,top)
            if(matrix[mid][0]<=target and matrix[mid][-1]>=target):
                row = mid 
                break
            elif(matrix[mid][0]>target):
                bottom = mid-1
            else:
                top = mid+1
            mid = (top+bottom)//2
        print(row)
        if row==-1:
            return False
        left = 0
        right = len(matrix[0])-1
        mid = (left+right)//2
        while(left<=right):
            if(matrix[row][mid]==target):
                return True
            elif(matrix[row][mid]>target):
                right = mid-1
            else:
                left = mid+1
            mid = (left+right)//2
        return False
        


        