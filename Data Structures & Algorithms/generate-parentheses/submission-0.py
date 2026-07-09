class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combo = []
        bracCount = {"(" : 0, ")" : 0}
        bracSum = 0
        def dfs():
            nonlocal bracSum

            if bracCount["("] == n and bracCount[")"] == n:
                res.append("".join(combo))

            if bracCount["("] < n:
                combo.append("(")
                bracCount["("] += 1
                bracSum += 1

                dfs()

                combo.pop()
                bracCount["("] -= 1
                bracSum -= 1

            if bracCount[")"] < n and bracSum > 0:
                combo.append(")")
                bracCount[")"] += 1
                bracSum -= 1

                dfs()

                combo.pop()
                bracCount[")"] -= 1
                bracSum += 1
        dfs()
        return res