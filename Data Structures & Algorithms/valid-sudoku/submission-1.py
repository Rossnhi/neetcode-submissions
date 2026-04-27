class Solution:
    def __init__(self):
        self.rowCheck = []
        self.colCheck = []
        self.boxCheck = []

    def isValidSudoku(self, board: List[List[str]]) -> bool:       
        for i in range(9):
            self.resetNumCheck()
            for j in range(9):
                # check row
                if board[i][j] != '.':
                    if self.rowCheck[int(board[i][j]) - 1]:
                        return False
                    else:
                        self.rowCheck[int(board[i][j]) - 1] = True

                # check column - board[j][i]
                if board[j][i] != '.':
                    if self.colCheck[int(board[j][i]) - 1]:
                        return False
                    else:
                        self.colCheck[int(board[j][i]) - 1] = True
                
                # check box - board[((i // 3) * 3) + (j // 3)][((i % 3) * 3) + (j % 3)]
                if board[((i // 3) * 3) + (j // 3)][((i % 3) * 3) + (j % 3)] != '.':    
                    if self.boxCheck[int(board[((i // 3) * 3) + (j // 3)][((i % 3) * 3) + (j % 3)]) - 1]:
                        return False
                    else:
                        self.boxCheck[int(board[((i // 3) * 3) + (j // 3)][((i % 3) * 3) + (j % 3)]) - 1] = True
        return True

    def resetNumCheck(self):
        self.rowCheck = [False, False, False, False, False, False, False, False, False]
        self.colCheck = [False, False, False, False, False, False, False, False, False]
        self.boxCheck = [False, False, False, False, False, False, False, False, False]
