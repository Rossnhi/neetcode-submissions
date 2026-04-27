class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        buckets = [[] for _ in range(10000)]
        for num in freqDict:
            buckets[freqDict[num] - 1].append(num)
        kFreq = []
        for i in range(1, len(buckets) + 1):
            if len(buckets[-i]) != 0:
                for num in buckets[-i]:
                    kFreq.append(num)
                    if len(kFreq) == k:
                        return kFreq