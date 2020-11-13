# 回溯算法 排列问题 记录状态
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        size = len(nums)
        check = [False] * size

        def dfs(path):
            if len(path) == size:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                check[i] = True
                dfs(path + [nums[i]])
                check[i] = False

        dfs([])
        return res
