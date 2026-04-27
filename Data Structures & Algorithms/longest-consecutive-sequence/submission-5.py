class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        next = defaultdict(int)
        out = 0
        for num in nums:
            if next[num] == 0:
                next[num] = next[num - 1] + next[num + 1] + 1
                next[num + next[num + 1]] = next[num]
                next[num - next[num - 1]] = next[num]
                out = max(out, next[num])
        return out