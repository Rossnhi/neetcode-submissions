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
                        if (x, y) in seen or x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[letter]:
                            return
                        letter += 1
                        seen.add((x, y))
                        for move in range(4):
                            dfs(x + int(math.cos(move * math.pi/2)), y + int(math.sin(move * math.pi/2)), letter, seen)
                        letter -= 1
                        seen.remove((x, y))
                    dfs(i, j, 0, set())
        return found