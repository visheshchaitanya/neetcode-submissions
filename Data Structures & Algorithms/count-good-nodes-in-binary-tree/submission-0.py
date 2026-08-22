# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: TreeNode, max_val: int) -> int:
        if root is None:
            return 0
        
        ans = 1 if root.val >= max_val else 0

        left_ans = self.helper(root.left, max(root.val, max_val))
        right_ans = self.helper(root.right, max(root.val, max_val))

        return ans + left_ans + right_ans
    
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.helper(root, root.val)
        