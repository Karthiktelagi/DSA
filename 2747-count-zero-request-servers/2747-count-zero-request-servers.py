from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs based on time
        logs.sort(key=lambda log: log[1])
        
        # Pair queries with their original indices and sort them by time
        qs = sorted([(q, i) for i, q in enumerate(queries)])
        
        ans = [0] * len(queries)
        cnt = {} # Maps server_id -> number of requests in current window
        
        left = 0
        right = 0
        
        for q_time, original_idx in qs:
            window_start = q_time - x
            
            # 1. Expand window: Add logs that occurred on or before the query time
            while right < len(logs) and logs[right][1] <= q_time:
                server = logs[right][0]
                cnt[server] = cnt.get(server, 0) + 1
                right += 1
                
            # 2. Shrink window: Remove logs that occurred before the window started
            while left < len(logs) and logs[left][1] < window_start:
                server = logs[left][0]
                cnt[server] -= 1
                if cnt[server] == 0:
                    del cnt[server] # Remove server entirely if it has no active requests
                left += 1
                
            # 3. Store result: total servers minus servers active in this window
            ans[original_idx] = n - len(cnt)
            
        return ans