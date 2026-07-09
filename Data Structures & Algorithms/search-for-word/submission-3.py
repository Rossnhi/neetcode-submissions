class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        for i in range(len(board)):
            if found:
                break
            for j in range(len(board[0])):
                if found:
                    break
                if board[i][j] == word[0]:
                    def dfs(x, y, letter, seen):
                        nonlocal found
                        if letter == len(word) or found:
                            found = True
                            return
                        for move in range(4):
                            if (x, y) in seen or x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[letter]:
                                continue
                            letter += 1
                            seen.add((x, y))

                            dfs(x + int(math.cos(move * math.pi/2)), y + int(math.sin(move * math.pi/2)), letter, seen.copy())

                            letter -= 1
                            seen.remove((x, y))
                    dfs(i, j, 0, set())
        return found