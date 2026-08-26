class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        delta = [-1, 0, 1, 0, -1]

        while q:
            curr_i, curr_j = q.popleft()

            for k in range(len(delta) - 1):
                new_i = curr_i + delta[k]
                new_j = curr_j + delta[k + 1]

                if (
                    0 <= new_i < m
                    and 0 <= new_j < n
                    and grid[new_i][new_j] == 2147483647
                ):
                    grid[new_i][new_j] = grid[curr_i][curr_j] + 1
                    q.append((new_i, new_j))