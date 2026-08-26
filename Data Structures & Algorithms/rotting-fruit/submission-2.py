class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        time = [[float('inf')]*n for _ in range(m)]

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    time[i][j] = 0
                    q.append((i, j))
                elif grid[i][j] == 0:
                    time[i][j] = -1
        
        delta = [-1, 0, 1, 0, -1]

        while q:
            curr = q.popleft()

            curr_i = curr[0]
            curr_j = curr[1]

            for i in range(len(delta) - 1):
                new_i = curr_i + delta[i]
                new_j = curr_j + delta[i + 1]

                if (
                    0 <= new_i < m 
                    and 0 <= new_j < n
                    and grid[new_i][new_j] == 1
                    and time[new_i][new_j] > time[curr_i][curr_j] + 1
                ):
                    time[new_i][new_j] = time[curr_i][curr_j] + 1
                    q.append((new_i, new_j))
        
        ans = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if time[i][j] == float('inf'):
                        return -1
                    ans = max(ans, time[i][j])
        
        return 0 if ans == -1 else ans

        