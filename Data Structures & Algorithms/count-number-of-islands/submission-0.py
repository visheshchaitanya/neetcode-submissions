class Solution:
    def dfs(self, grid, visited, i, j):
        if i >= len(grid) or j >= len(grid[0]):
            return

        visited[i][j] = True
        options = [-1, 0, 1, 0, -1]

        for x in range(len(options)-1):
            deli = options[x]
            delj = options[x+1]

            if i + deli >= 0 and i + deli < len(grid) and j + delj >= 0 and j + delj < len(grid[0]) and grid[i + deli][j + delj] == '1' and visited[i + deli][j + delj] == False:
                self.dfs(grid, visited, i + deli, j + delj)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j] == False:
                    self.dfs(grid, visited, i, j)
                    ans += 1
        
        return ans

        