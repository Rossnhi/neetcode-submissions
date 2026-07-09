class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
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
                        nonlocal dirs
                        if (x, y) in seen or x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[letter]:
                            return

                        if letter == len(word) - 1 or found:
                            found = True
                            return

                        letter += 1
                        seen.add((x, y))
                        for dx, dy in dirs:
                            dfs(x + dx, y + dy, letter, seen)
                        letter -= 1
                        seen.remove((x, y))
                    dfs(i, j, 0, set())
        return found