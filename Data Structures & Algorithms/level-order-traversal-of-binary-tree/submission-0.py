# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = deque()
        ans = []

        q.append(root)

        while len(q) != 0:
            curr = []
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                curr.append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
            
            ans.append(curr)
        
        return ans
        