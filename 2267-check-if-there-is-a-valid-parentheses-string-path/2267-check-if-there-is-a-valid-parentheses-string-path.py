class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        path_len = m + n - 1
        
        # A valid parentheses string must be of even length
        if path_len % 2 == 1:
            return False
            
        # A valid path must start with '(' and end with ')'
        if grid[0][0] != '(' or grid[n-1][m-1] != ')':
            return False
            
        dp = [[0] * m for _ in range(n)]
        
        # Base case: bit index 1 represents a balance of +1
        dp[0][0] = 1 << 1
        
        for i in range(n):
            for j in range(m):
                change = 1 if grid[i][j] == "(" else -1
                
                # Check path from the cell above
                if i > 0:
                    if change == 1:
                        dp[i][j] |= dp[i-1][j] << 1
                    else:
                        dp[i][j] |= dp[i-1][j] >> 1
                        
                # Check path from the cell to the left
                if j > 0:
                    if change == 1:
                        dp[i][j] |= dp[i][j-1] << 1
                    else:
                        dp[i][j] |= dp[i][j-1] >> 1
                        
        # Check if the 0th bit (balance of exactly 0) is set at the destination
        return bool(dp[-1][-1] & 1)