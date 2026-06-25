class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowDigits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            columnDigits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            boxDigits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for j in range(9):
                #row - board[i][j]
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if num in rowDigits:
                        rowDigits.remove(num)
                    else:
                        return False

                # column - board[j][i]
                if board[j][i] != ".":
                    num = int(board[j][i])
                    if num in columnDigits:
                        columnDigits.remove(num)
                    else:
                        return False
                
                # box - board[(i // 3) * 3 + (j // 3)][(i % 3) * 3) + (j % 3)]
                if board[(i // 3) * 3 + (j // 3)][((i % 3) * 3) + (j % 3)] != ".":
                    num = int(board[(i // 3) * 3 + (j // 3)][((i % 3) * 3) + (j % 3)])
                    if num in boxDigits:
                        boxDigits.remove(num)
                    else:
                        return False
        return True