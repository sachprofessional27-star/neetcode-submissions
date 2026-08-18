import copy
class Solution:
    def rec(self,board,x,y,idx,word,flag,orignal):
        
        if(idx==len(word)):
            flag = True
            return flag
        if(x<0 or x>=len(board) or y<0 or y>=len(board[0])):
            return flag
        if(board[x][y]=="-1"):
            return flag
        
        if(board[x][y]!=word[idx]):
            return flag
        
        board[x][y]="-1"
     
        flag = self.rec(board,x+1,y,idx+1,word,flag,orignal)
        if(flag!=True):
            flag = self.rec(board,x-1,y,idx+1,word,flag,orignal)
            
        if(flag!=True):
            flag = self.rec(board,x,y+1,idx+1,word,flag,orignal)
            
        if(flag!=True):
            flag = self.rec(board,x,y-1,idx+1,word,flag,orignal)
            
        board[x][y]=orignal[x][y]
        return flag
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j]==word[0]):
                    temp = copy.deepcopy(board)
                    ans = self.rec(temp,i,j,0,word,ans,board)
                    if(ans==True):
                        return True
        return False


        