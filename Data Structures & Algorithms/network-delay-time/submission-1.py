class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n
        pq = []
        adjlist = [[] for _ in range(n)]

        for time in times:
            ui = time[0]-1
            vi = time[1]-1
            ti = time[2]

            adjlist[ui].append((vi, ti))
        
        heapq.heappush(pq, (0, k-1));
        dist[k-1] = 0

        while pq:
            curr = heapq.heappop(pq)

            curr_dist = curr[0]
            curr_node = curr[1]

            for edge in adjlist[curr_node]:
                if dist[edge[0]] > curr_dist + edge[1]:
                    dist[edge[0]] = curr_dist + edge[1]
                    heapq.heappush(pq, (dist[edge[0]], edge[0]))
            
        ans = 0
        for curr in dist:
            if curr == float('inf'):
                return -1
            ans = max(ans, curr)
        return ans
            
        