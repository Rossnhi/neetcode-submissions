class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        total = 0
        combo = []
        def dfs(n):
            nonlocal total
            if total >= target:
                if total == target:
                    res.append(combo.copy())
                return
            for i in range(n, len(nums)):
                if total + nums[i] > target:
                    break
                combo.append(nums[i])
                total += nums[i]
                dfs(i)
                combo.pop()
                total -= nums[i]
        dfs(0)
        return res