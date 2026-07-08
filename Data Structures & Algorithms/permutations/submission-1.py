class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        def dfs(seenIndex):
            if len(seenIndex) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if i not in seenIndex:
                    perm.append(nums[i])
                    seenIndex.add(i)

                    dfs(seenIndex)

                    perm.pop()
                    seenIndex.remove(i)
        dfs(set())
        return res