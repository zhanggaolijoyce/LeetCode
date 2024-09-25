class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = set()
        for root in dictionary:
            st = ""
            for ch in root:
                st += ch
                if st in s:
                    break
            s.add(st)

        ls = sentence.split()
        res = []
        for word in ls:
            st = ""
            for ch in word:
                st += ch
                if st in s:
                    break
            res.append(st)
        return " ".join(res)
