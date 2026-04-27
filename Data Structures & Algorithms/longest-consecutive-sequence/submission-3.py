class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = defaultdict(int)
        longest = 0
        for num in nums:
            if sequence[num] == 0:
                sequence[num] = sequence[num - 1] + sequence[num + 1] + 1
                sequence[num + sequence[num + 1]] = sequence[num]
                sequence[num - sequence[num - 1]] = sequence[num]
            longest = max(longest, sequence[num])
        return longest
            