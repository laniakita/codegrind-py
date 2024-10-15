# Definition for a binary tree node.
from typing import Optional
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = sys.maxsize
        def inorder(node, lower, upper):
            if not node:
                return True
            if lower < node.val < upper:
                return inorder(node.left, lower, node.val) and inorder(node.right, node.val, upper)
            else:
                return False
        return inorder(root, -INF, INF)

Solution().isValidBST(tree)       
        
        


