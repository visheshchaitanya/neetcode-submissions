# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        q = deque()
        q.append(root)
        ans = []

        while q:
            length = len(q)
            for i in range(length):
                curr = q.popleft()

                if i == length - 1:
                    ans.append(curr.val)
                
                if curr.left is not None:
                    q.append(curr.left)

                if curr.right is not None:
                    q.append(curr.right)
        
        return ans

        