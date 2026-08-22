# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: TreeNode, min_val : Optional[int], max_val : Optional[int]) -> bool:
        if root is None:
            return True
        
        left_ans = self.helper(root.left, min_val, root.val)
        right_ans = self.helper(root.right, root.val, max_val)

        ans = False
        if min_val is None and max_val is None:
            ans = True
        elif min_val is not None and max_val is not None:
            ans = True if root.val > min_val and root.val < max_val else False
        elif min_val is None:
            ans = True if root.val < max_val else False
        else:
            ans = True if root.val > min_val else False
        
        return ans and left_ans and right_ans


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return true
        
        return self.helper(root, None, None);
        