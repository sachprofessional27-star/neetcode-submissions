class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if(matrix[i][j]==0):
                    for k in range(0,len(matrix)):
                        if(matrix[k][j]!=0):
                            matrix[k][j]=float('inf')
                    for k in range(0,len(matrix[0])):
                        if(matrix[i][k]!=0):
                            matrix[i][k]=float('inf')
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(matrix[i][j]==float('inf')):
                    matrix[i][j]=0        
        