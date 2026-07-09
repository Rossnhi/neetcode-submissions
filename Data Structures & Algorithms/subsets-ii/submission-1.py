class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        sub = []
        def dfs(n):
            for i in range(n, len(nums)):
                if i > n and nums[i] == nums[i - 1]:
                    continue
                sub.append(nums[i])
                res.append(sub.copy())

                dfs(i + 1)

                sub.pop()
        dfs(0)
        return res