# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cur, stack, res = root, [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            tmp = stack.pop()
            cur = tmp.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cur, stack, res = root, [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            res.append(tmp.val)
            cur = tmp.right
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cur, stack, res = root, [], []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            tmp = stack.pop()
            cur = tmp.left
        return res[::-1]
