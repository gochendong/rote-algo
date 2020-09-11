"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrace(num, s, tmp):
            l = len(tmp)
            if s == n and l == k:
                res.append(tmp)
                return
            if num == 10 or s > n or l > k:
                return
            backtrace(num + 1, s + num, tmp + [num])
            backtrace(num + 1, s, tmp)

        backtrace(1, 0, [])
        return res
