from typing import List


class Solution:
    # 最大岛屿面积
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(
                x, y + 1)

        res = 0
        for x in range(m):
            for y in range(n):
                res = max(res, dfs(x, y))
        return res

    # 岛屿数量
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = "0"
            for i in range(4):
                nx, ny = x + directions[i], y + directions[i + 1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                    dfs(nx, ny)

        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    res += 1
                    dfs(x, y)
        return res
