##Memory Limit Exceeded 76 / 94 testcases passed

from typing import List, Optional
from collections import deque


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def path(a, b):
            p = 0
            if a == 0:
                p += 1
            if a == m-1:
                p += 1
            if b == 0:
                p+= 1
            if b == n-1:
                p += 1
            return p
        
        if maxMove == 0:
            return 0
        res = 0
        num = [[0]*n for _ in range(m)]
        
        for i in range(0, m):
            for j in range(0, n):
                num[i][j] = path(i, j)
        
        q = deque()
        q.append((startRow, startColumn, 0))
        move =  0
        while q:
            x, y, move = q.popleft()
            res += num[x][y]
            
            if move < maxMove - 1:
                if x+1 < m:
                    q.append((x+1, y, move+1))
                if x-1 >= 0:
                    q.append((x-1, y, move+1))
                if y+1 < n:
                    q.append((x, y+1, move+1))
                if y-1 >= 0:
                    q.append((x, y-1, move+1))
        return res%(10**9+7)  
