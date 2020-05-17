class Solution:
    steps = ((-1, 0), (0, 1), (1, 0), (0, -1))
    def _dfs(self, i, j, N, M, grid, visited, cnt, total, ans):
        if grid[i][j] == 2:
            ans[0] += total == cnt - 1
            return

        visited[i][j] = True
        for di, dj in Solution.steps:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and grid[ni][nj] != -1:
                self._dfs(ni, nj, N, M, grid, visited, cnt + 1, total, ans)
        visited[i][j] = False

    def uniquePathsIII(self, grid):
        if not grid:
            return 0

        N, M = len(grid), len(grid[0])
        startI = startJ = -1
        total = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    startI, startJ = i, j
                elif grid[i][j] == 0:
                    total += 1

        result = [0]
        visited = [[False] * M for _ in range(N)]

        self._dfs(startI, startJ, N, M, grid, visited, 0, total, result)
        return result[0]


if __name__ == "__main__":
    print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
    print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
    print(Solution().uniquePathsIII([[0, 1], [2, 0]]))