class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        largestSeqLen = 0
        for num in nums:
            numSeq = 1
            if num - 1 not in numSet:
                while numSeq < len(nums):
                    if num + numSeq in numSet:
                        numSeq += 1
                    else:
                        break
                if numSeq > largestSeqLen:
                    largestSeqLen = numSeq
        return largestSeqLen