class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowDict = {
            1 : False,
            2 : False,
            3 : False,
            4 : False,
            5 : False,
            6 : False,
            7 : False,
            8 : False,
            9 : False
            }
            columnDict = {
            1 : False,
            2 : False,
            3 : False,
            4 : False,
            5 : False,
            6 : False,
            7 : False,
            8 : False,
            9 : False
            }
            boxDict = {
            1 : False,
            2 : False,
            3 : False,
            4 : False,
            5 : False,
            6 : False,
            7 : False,
            8 : False,
            9 : False
            }
            for j in range(9):
                #row
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    if rowDict[num]:
                        return False
                    else:
                        rowDict[num] = True
                #column
                num = board[j][i]
                if num != ".":
                    num = int(num)
                    if columnDict[num]:
                        return False
                    else:
                        columnDict[num] = True
                #box
                num = board[ (i // 3) * 3+ j // 3][(i % 3) * 3 + j % 3]
                if num != ".":
                    num = int(num)
                    if boxDict[num]:
                        return False
                    else:
                        boxDict[num] = True
        return True











