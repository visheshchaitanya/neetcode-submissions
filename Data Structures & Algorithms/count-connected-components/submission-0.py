class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, n: int) -> int:
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, i: int, j: int) -> bool:
        ulp_i = self.find(i)
        ulp_j = self.find(j)

        if ulp_i == ulp_j:
            return False
        
        if self.size[ulp_i] >= self.size[ulp_j]:
            self.parent[ulp_j] = ulp_i
            self.size[ulp_i] += 1
        else:
            self.parent[ulp_i] = ulp_j
            self.size[ulp_j] += 1
        
        return True
    
    def connected(self) -> int:
        count = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                count += 1
        
        return count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for edge in edges:
            if dsu.union(edge[0], edge[1]):
                res -= 1
        return res
        