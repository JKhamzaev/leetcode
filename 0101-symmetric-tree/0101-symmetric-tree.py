# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symmetric(self, a, b):
        if not a and not b:
            return True
        
        if not a or not b:
            return False

        if a.val != b.val:
            return False

        return self.symmetric(a.left, b.right) and self.symmetric(a.right, b.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric(root, root)