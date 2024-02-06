class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = {}
        ls1 = {}
        for ele in strs:
            if ele in ls:
                ls1[ele] = ls1.get(ele, 0)+1
                continue
            d = {}
            for char in ele:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1
            ls[ele] = d
        
        
        res = []
        for ele in ls1:
            res.append([ele for _ in range(ls1[ele])])
        for ele in ls:
            if not res:
                res.append([ele])
            
            else:
                exist = False
                for group in res:
                    if ls[ele] == ls[group[0]]:
                        group.append(ele)
                        exist = True
                        break
                if not exist:
                    res.append([ele])
        
    
        return res
        
