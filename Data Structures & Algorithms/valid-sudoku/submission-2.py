class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [False for _ in range(9)]
            column = [False for _ in range(9)]
            box = [False for _ in range(9)]
            for j in range(9):
                # row [i][j]
                if board[i][j] != ".":
                    if row[int(board[i][j]) - 1]:
                        return False
                    row[int(board[i][j]) - 1] = True
                # column [j][i]
                if board[j][i] != ".":
                    if column[int(board[j][i]) - 1]:
                        return False
                    column[int(board[j][i]) - 1] = True
                # box [(i // 3) * 3 + (j // 3)][((i % 3) * 3) + (j % 3)]
                if board[(i // 3) * 3 + (j // 3)][((i % 3) * 3) + (j % 3)] != ".":
                    if box[int(board[(i // 3) * 3 + (j // 3)][((i % 3) * 3) + (j % 3)]) - 1]:
                        return False
                    box[int(board[(i // 3) * 3 + (j // 3)][((i % 3) * 3) + (j % 3)]) - 1] = True
        return True