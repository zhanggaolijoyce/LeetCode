class Solution:
    def frequencySort(self, s: str) -> str:
        ls = set()
        d1 = {}
        for char in s:
            d1[char] = d1.get(char, 0)+1
        
        for num in d1.values():
            ls.add(num)
        
        ls = list(ls)
        ls = sorted(ls, reverse=True)

        d2 = {}
        for char, num in d1.items():
            d2[num] = d2.get(num, [])
            d2[num].append(char)
        
        s1 = ""
        for i in ls:
            for j in d2[i]:
                s1 += "".join(j*i)

        return s1
