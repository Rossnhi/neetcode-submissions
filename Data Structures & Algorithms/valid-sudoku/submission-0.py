class Solution:
    def __init__(self):
        self.numCheck = {}

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            self.resetNumCheck()
            for num in row:
                # check row
                if num == '.':
                    continue
                if self.numCheck[num]:
                    return False
                else:
                    self.numCheck[num] = True
        for i in range(9):
            self.resetNumCheck()
            for j in range(9):
                # check column - board[j][i]
                if board[j][i] == '.':
                    continue
                if self.numCheck[board[j][i]]:
                    return False
                else:
                    self.numCheck[board[j][i]] = True
        for i in range(9):
            self.resetNumCheck()
            for j in range(9):
                # check box - board[((i // 3) * 3) + (j // 3)][((i % 3) * 3) + (j % 3)]
                if board[((i // 3) * 3) + (j // 3)][((i % 3) * 3) + (j % 3)] == '.':
                    continue
                if self.numCheck[board[((i // 3) * 3) + (j // 3)][((i % 3) * 3) + (j % 3)]]:
                    return False
                else:
                    self.numCheck[board[((i // 3) * 3) + (j // 3)][((i % 3) * 3) + (j % 3)]] = True
        return True

    def resetNumCheck(self):
        self.numCheck = {
            '1' : False,
            '2' : False,
            '3' : False,
            '4' : False,
            '5' : False,
            '6' : False,
            '7' : False,
            '8' : False,
            '9' : False
        }
