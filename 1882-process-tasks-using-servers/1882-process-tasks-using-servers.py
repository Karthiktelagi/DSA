import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # available: (weight, index)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)
        
        # busy: (free_time, weight, index)
        busy = []
        res = []
        time = 0
        
        for i, task_duration in enumerate(tasks):
            time = max(time, i)
            
            # Fast-forward time if all servers are busy
            if not available:
                time = busy[0][0]
            
            # Free up servers that are done processing
            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))
                
            # Assign task to the optimal available server
            weight, index = heapq.heappop(available)
            res.append(index)
            heapq.heappush(busy, (time + task_duration, weight, index))
            
        return res