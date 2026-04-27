class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        allZeroes = True
        zeroInNums = False
        prod = 1
        for num in nums:
            if num != 0:
                allZeroes = False
                prod *= num
            else:
                if zeroInNums:
                    prod *= num
                else:
                    zeroInNums = True
        out = []
        for num in nums:
            if num != 0:
                if zeroInNums:
                    out.append(0)
                else:
                    out.append(prod//num)
            else:
                out.append(prod)
        return out