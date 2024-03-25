class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num += 1
                    dq = deque()
                    dq.append([i, j])
                    while dq:
                        m,n = dq.popleft()
                        grid[m][n] = -1
                        if m > 0 and grid[m-1][n] == '1':
                            grid[m-1][n] = -1
                            dq.append([m-1, n])
                        if m+1 < len(grid) and grid[m+1][n] == '1':
                            grid[m+1][n] = -1
                            dq.append([m+1, n])
                        if n > 0 and grid[m][n-1] == '1':
                            grid[m][n-1] = -1
                            dq.append([m, n-1])
                        if n+1 < len(grid[0]) and grid[m][n+1] == '1':
                            grid[m][n+1] = -1
                            dq.append([m, n+1])
             
        return num
