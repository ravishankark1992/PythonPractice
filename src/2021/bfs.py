from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return False


def main():

    solution_object = Solution()
    # root = [5,1,4,null,null,3,6]
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    # root = TreeNode(val, left, right)
    # solution_object.isValidBST(root)
