class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        minH = []
        for i in range(n):
            dist = math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)**2)
            heapq.heappush(minH, (dist, i))
        
        ans = []
        count = 0
        while (count < k):
            ans.append(points[heapq.heappop(minH)[1]])
            count += 1
        
        return ans
        