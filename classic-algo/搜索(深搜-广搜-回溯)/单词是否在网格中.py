# 回溯算法, 搜索问题, 记录状态
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [-1, 0, 1, 0, -1]
        visited = [[0] * n for i in range(m)]

        def dfs(x, y, idx):
            if board[x][y] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            visited[x][y] = 1
            for i in range(4):
                nx, ny = x + directions[i], y + directions[i + 1]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and dfs(
                        nx, ny, idx + 1):
                    return True
            visited[x][y] = 0
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
