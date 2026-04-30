class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        res = ""
        if len(strs) // 100 == 0:
            res += "0"
        if len(strs) // 10 == 0:
            res += "0"
        res += str(len(strs))
        concat = ""
        for s in strs:
            if len(s) // 100 == 0:
                res += "0"
            if len(s) // 10 == 0:
                res += "0"
            res += str(len(s))
            concat += s
        return res + concat

    def decode(self, s: str) -> List[str]:
        n = int(s[0:3])
        j = (3 * (n + 1))
        res = []
        for i in range(1, n + 1):
            l = int(s[(i * 3) : ((i + 1) * 3)])
            res.append(s[j : j + l])
            j += l
        return res