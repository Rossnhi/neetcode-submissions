class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        freqDict = {}
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        for num in freqDict:
            freq[freqDict[num]].append(num)
        out = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i] != []:
               for num in freq[i]:
                    if len(out) < k:
                        out.append(num)
            if len(out) == k:
                return out