class Solution:
    def bfs(self, grid, i, j, m, n):
        q = deque()
        q.append((0, (i, j)))

        while q:
            curr = q.popleft()

            dist = curr[0]
            curr_i = curr[1][0]
            curr_j = curr[1][1]

            delta = [-1, 0, 1, 0, -1]
            for i in range(len(delta) - 1):
                del_i = delta[i]
                del_j = delta[i + 1]

                new_i = curr_i + del_i
                new_j = curr_j + del_j

                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] > dist + 1:
                    grid[new_i][new_j] = dist + 1
                    q.append((dist + 1, (new_i, new_j)))



    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.bfs(grid, i, j, m, n)

        