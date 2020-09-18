"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        size = len(nums)
        visited = [False] * size
        path = []

        def dfs():
            if len(path) == size:
                res.append(path[:])
                return
            for i, num in enumerate(nums):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                path.append(num)
                dfs()
                path.pop()
                visited[i] = False

        dfs()
        return res
