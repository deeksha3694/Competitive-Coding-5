class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        
        valid =  True 
        
        
        #check the board is valid
        if(board == 0 or len(board) != 9 or len(board[0]) != 9):
            return False
        
        #check the row is valid 
        for i in range(row):
            checklist = {}
            for j in range(col):
                if (board[i][j] == '.'):
                    continue
                elif board[i][j] in checklist.keys():
                    valid = False
                    return valid
                elif board[i][j] < '1' or board[i][j] > '9':
                    valid = False
                    return valid
                else:
                    checklist[board[i][j]] = True
                    
        #check the column is valid
        for j in range(col):
            checklist = {}
            for i in range(row):
                if (board[i][j] == '.'):
                    continue
                elif board[i][j] in checklist.keys():
                    valid = False
                    return valid
                elif board[i][j] < '1' or board[i][j] > '9':
                    valid = False
                    return valid
                else:
                    checklist[board[i][j]] = True
                    
        #check for the 3X3 block
        for i in range(3):
            for j in range(3):
                checklist = {}
                row = i*3
                col = j*3
                for k in range(row, row+3):
                    for h in range(col, col+3):
                        if(board[k][h] == '.'):
                            continue
                        elif board[k][h] < '1' or board[k][h] > '9':
                            valid = False
                            return valid
                        elif board[k][h] in checklist.keys():
                            valid = False
                            return valid
                        else: 
                            checklist[board[k][h]] = True
        return valid
            