import copy
class Solution:
    def validate(self,x,y,board):
        for i in range(0,len(board)):
            if(i!=x and board[i][y]=="Q"):
                return False
            if(i!=y and board[x][i]=="Q"):
                return False
        p = x-1
        q = y-1
        while(p>=0 and q>=0):
            if(board[p][q]=='Q'):
                return False
            p-=1
            q-=1
        p = x+1
        q = y+1
        while(p<len(board) and q<len(board[0])):
            if(board[p][q]=='Q'):
                return False
            p+=1
            q+=1
        p = x+1
        q = y-1
        while(p<len(board) and q>=0):
            if(board[p][q]=='Q'):
                return False
            p+=1
            q-=1
        p = x-1
        q = y+1
        while(p>=0 and q<len(board)):
            if(board[p][q]=='Q'):
                return False
            p-=1
            q+=1
        return True
    
    def place_queens(self,board,col,answer):
        if(col>=len(board)):
           
            answer.append(copy.deepcopy(board))
            return
        for i in range(0,len(board)):
            if(self.validate(i,col,board)):
                board[i][col]='Q'
                self.place_queens(board,col+1,answer)
                board[i][col]='.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        answer = []
        self.validate(0,0,board)
        for i in range(0,n):
            k = []
            for j in range(0,n):
                k.append('.')
            board.append(k)
        self.place_queens(board,0,answer)
        ans = []
        for i in range(0,len(answer)):
            arr = []
            for j in range(0,len(board)):
                s = ""
                for k in range(0,len(board)):
                    s+=answer[i][j][k]
                arr.append(s)
            ans.append(arr)
        return ans
        
                
        