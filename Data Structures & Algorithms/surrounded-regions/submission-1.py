class Solution:
    def marker(self,board,x,y):
        if(x<0 or y<0 or x>=len(board) or y>=len(board[0])):
            return
        if(board[x][y]=="-1" or board[x][y]=="X"):
            return
        board[x][y]="-1"
        self.marker(board,x+1,y)
        self.marker(board,x-1,y)
        self.marker(board,x,y+1)
        self.marker(board,x,y-1)
    def solve(self, board: List[List[str]]) -> None:
        for i in range(0,len(board)):
            if(board[i][0]=="O"):
                self.marker(board,i,0)
            if(board[i][len(board[0])-1]=="O"):
                self.marker(board,i,len(board[0])-1)
        for j in range(0,len(board[0])):
            if(board[0][j]=="O"):
                self.marker(board,0,j)
            if(board[len(board)-1][j]=="O"):
                self.marker(board,len(board)-1,j)

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j]=="-1"):
                    board[i][j]="O"
                elif(board[i][j]=="O"):
                    board[i][j]="X"

