class Solution:
    def dfs(self, grid, visited, i, j):
        visited[i][j] = True
        options = [-1, 0, 1, 0, -1]
        ans = 1

        for x in range(len(options)-1):
            deli = options[x]
            delj = options[x+1]

            if i + deli >= 0 and i + deli < len(grid) and j + delj >= 0 and j + delj < len(grid[0]) and grid[i + deli][j + delj] == 1 and visited[i + deli][j + delj] == False:
                ans += self.dfs(grid, visited, i + deli, j + delj)
            
        return ans
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False]*n for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    ans = max(ans, self.dfs(grid, visited, i, j))
        
        return ans
        