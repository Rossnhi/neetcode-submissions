class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sum = 0
        combo = []
        def dfs(n):
            nonlocal sum
            if sum >= target:
                if sum == target:
                    res.append(combo.copy())
                return
            for i in range(n, len(nums)):
                combo.append(nums[i])
                sum += nums[i]
                dfs(i)
                combo.remove(nums[i])
                sum -= nums[i]
        dfs(0)
        return res