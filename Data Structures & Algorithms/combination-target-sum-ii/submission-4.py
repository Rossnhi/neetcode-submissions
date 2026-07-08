class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        total = 0
        combo = []
        def dfs(n):
            nonlocal total
            if total >= target:
                if total == target:
                    res.append(combo.copy())
                return
            for i in range(n, len(candidates)):
                if i > n and candidates[i] == candidates[i - 1]:
                    continue

                total += candidates[i]
                combo.append(candidates[i])

                dfs(i + 1)

                total -= candidates[i]
                combo.pop()
        dfs(0)
        return res