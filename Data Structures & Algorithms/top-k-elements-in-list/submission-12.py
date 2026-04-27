class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        freqBucket = [[] for _ in range(10000)]
        for num in freq:
            freqBucket[freq[num]].append(num)
        out = []
        for i in range(len(freqBucket) - 1, -1, -1):
            for num in freqBucket[i]:
                out.append(num)
                if len(out) == k:
                    return out