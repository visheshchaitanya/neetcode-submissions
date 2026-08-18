class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ulp_a = self.find(a)
        ulp_b = self.find(b)

        if ulp_a == ulp_b:
            return False
        
        if self.rank[ulp_a] >= self.rank[ulp_b]:
            self.parent[ulp_b] = ulp_a
            self.rank[ulp_a] += 1
        else:
            self.parent[ulp_a] = ulp_b
            self.rank[ulp_b] += 1
        
        return True
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)




class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total_points = len(points)
        distance_list = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    a = points[i]
                    b = points[j]

                    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
                    distance_list.append((dist, i, j))
        
        distance_list.sort()
        
        dsu = DSU(total_points)
        min_weight = 0
        
        for i in range(len(distance_list)):
            curr = distance_list[i]
            mh_dist = curr[0]
            
            if dsu.is_connected(curr[1], curr[2]):
                continue
            
            dsu.union(curr[1], curr[2])
            min_weight += mh_dist
        
        return min_weight


        