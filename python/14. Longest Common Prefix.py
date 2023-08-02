class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        res = ""
        if l == 1:
            return strs[0]
        else:
            for i in range(0, min(len(strs[0]), len(strs[1]))):
                if strs[0][i] == strs[1][i]:
                    res += strs[0][i]
                else:
                    break
            for j in range(2, l):
                res = res[0:min(len(res), len(strs[j]))]
                for k in range(0, len(res)):
                    if strs[j][k] != res[k]:
                        res = res[0: k]
                        break
            return res
