import bisect
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Keeps track of (free_time, server_id) for busy servers
        busy = []
        
        # Maintains currently available server IDs in sorted order
        free_servers = list(range(k))
        
        # Count of successful requests handled by each server
        request_counts = [0] * k
        
        for i, start_time in enumerate(arrival):
            # 1. Free up servers whose tasks have finished by the current arrival time
            while busy and busy[0][0] <= start_time:
                _, freed_server = heapq.heappop(busy)
                # Insert back into the sorted free list while maintaining order
                bisect.insort(free_servers, freed_server)
            
            # If no servers are available, drop the request
            if not free_servers:
                continue
                
            # 2. Find the preferred server using binary search (>= i % k)
            target = i % k
            idx = bisect.bisect_left(free_servers, target)
            
            # If no server >= target is free, wrap around to the first available server (index 0)
            if idx == len(free_servers):
                idx = 0
                
            server = free_servers.pop(idx)
            
            # 3. Assign the request
            request_counts[server] += 1
            heapq.heappush(busy, (start_time + load[i], server))
            
        # 4. Find the maximum requests handled by any server
        max_handled = max(request_counts)
        
        # Return all servers that hit this maximum count
        return [i for i, count in enumerate(request_counts) if count == max_handled]