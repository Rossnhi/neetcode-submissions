class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        buckets = [[] for i in range(len(nums) + 1)]
        for num in freqDict:
            buckets[freqDict[num]].append(num)
        out = []
        print(buckets)
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i] != []:
                for num in buckets[i]:
                    if len(out) < k:
                        out.append(num)
                    else:
                        return out
        return out