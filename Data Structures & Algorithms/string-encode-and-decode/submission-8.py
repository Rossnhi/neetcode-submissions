class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#"
            res += s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        l =[]
        n = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                n += s[i]
                i += 1
            else:
                n = int(n)
                l.append(s[i + 1 : i + n + 1])
                i = i + n + 1
                n = ""
        return l