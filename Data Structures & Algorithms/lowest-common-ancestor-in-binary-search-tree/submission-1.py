# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return root
        
        if root.val == p.val or root.val == q.val:
            return root

        left_check = self.lowestCommonAncestor(root.left, p, q)
        right_check = self.lowestCommonAncestor(root.right, p, q)

        if left_check is not None and right_check is not None:
            return root
        elif left_check is not None:
            return left_check
        else:
            return right_check
        