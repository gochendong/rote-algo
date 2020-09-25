"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

来源：力扣（LeetCode）
链接：
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrace(candidates, tmp):
            if sum(tmp) == target:
                res.append(tmp)
                return
            if sum(tmp) > target:
                return
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                backtrace(candidates[i + 1:], tmp + [candidates[i]])

        backtrace(candidates, [])
        return res
