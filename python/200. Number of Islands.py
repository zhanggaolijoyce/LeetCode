class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num += 1
                    grid[i][j] = "0"
                    dq = deque()
                    dq.append([i, j])
                    while dq:
                        p, q = dq.popleft()
                        for a,b in ([p-1, q],[p+1, q], [p, q-1], [p, q+1]):
                            if 0<=a<m and 0<=b<n and grid[a][b] == "1":
                                grid[a][b] = "0"
                                dq.append([a, b])
        return num

        
