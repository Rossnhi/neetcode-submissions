class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        freqList =[k[0] for k in sorted(freqDict.items(), key=lambda item: item[1], reverse = True)]
        return freqList[0:k]