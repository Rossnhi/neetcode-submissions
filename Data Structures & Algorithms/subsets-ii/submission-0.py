class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        sub = []
        def dfs(n, seen):
            for i in range(n, len(nums)):
                if nums[i] in seen:
                    continue
                sub.append(nums[i])
                res.append(sub.copy())

                dfs(i + 1, seen.copy())

                sub.pop()
                seen.add(nums[i])
        dfs(0, set())
        return res