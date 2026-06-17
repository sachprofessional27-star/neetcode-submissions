from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board)):
            row_arr = set()
            for j in range(0,len(board[i])):
                if(board[i][j]=='.'):
                    pass
                elif(int(board[i][j])>9 or int(board[i][j])<1):
                    return(False)
                else:
                    prior = len(row_arr)
                    row_arr.add(board[i][j])
                    post = len(row_arr)
                    if(prior == post):
                        return(False)
            col_arr = set()
            for j in range(0,len(board)):
                if(board[j][i]=='.'):
                    pass
                elif(int(board[j][i])>9 or int(board[j][i])<1):
                    return(False)
                else:
                    prior = len(col_arr)
                    col_arr.add(board[j][i])
                    post = len(col_arr)
                    if(prior == post):
                        return(False)
        
        for i in (0,3,6):
            for j in (0,3,6):
                box_set = set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if(board[k][l]=='.'):
                            pass
                        else:
                            var = int(board[k][l])
                            if(var>9 or var<1):
                                return(False)
                            else:
                                prior= len(box_set)
                                box_set.add(var)
                                post = len(box_set)
                                if(prior == post):
                                    return(False)
        return(True)

        #return(False)
        