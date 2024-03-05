class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        k = 0
        res = []
        while k < n-1:
            l = len(words[k])
            ls = [k]
            while k<n-1 and l+len(words[k+1])+1 <= maxWidth:
                k += 1
                l += len(words[k])+1
                ls.append(k)
            s = ""
            l1 = len(ls)-1
            l2 = maxWidth - sum(len(words[i]) for i in ls)
            for i in ls:
                s += words[i]
                if l1 > 0:
                    s += " "*ceil(l2/l1)
                    l2 -= ceil(l2/l1)
                    l1 -= 1
                else:
                    s += " "*l2
            res.append(s)
            k += 1
        if k == n-1:
            res.append(words[k]+(maxWidth-len(words[k]))*" ")
        elif k == n:
            res.pop()
            s = " ".join(words[j] for j in ls)
            s += " "* (maxWidth-len(s))
            res.append(s)
        return res
