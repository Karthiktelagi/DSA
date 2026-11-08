class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_counts = [0] * m
        col_counts = [0] * n
        
        # Pass 1: Count servers in each row and column
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
                    
        ans = 0
        
        # Pass 2: Check if a server can communicate
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (row_counts[r] > 1 or col_counts[c] > 1):
                    ans += 1
                    
        return ans