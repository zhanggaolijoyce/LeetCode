class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(i):
            if color[i] == 0:
                color[i] = 1
            for j in ls[i]:
                if color[j] == 0:
                    color[j] = -color[i]
                    if not dfs(j):
                        return False
                else:
                    if color[j] == color[i]:
                        return False
            return True


        ls = [[] for _ in range(n)]
        for a,b in dislikes:
            ls[a-1].append(b-1)
            ls[b-1].append(a-1)
        
        color = [0] * n
        
        for i in range(n):
            if color[i] == 0:
                res = dfs(i)
                if not res:
                    return False
        return True
