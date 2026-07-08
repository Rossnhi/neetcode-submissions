class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0
        combo = []
        def dfs(n, seen):
            nonlocal total
            if total >= target:
                if total == target:
                    res.append(combo.copy())
                return
            for i in range(n, len(candidates)):
                if candidates[i] in seen:
                    continue

                total += candidates[i]
                combo.append(candidates[i])

                dfs(i + 1, seen.copy())

                total -= candidates[i]
                combo.pop()
                seen.add(candidates[i])
        dfs(0, set())
        return res