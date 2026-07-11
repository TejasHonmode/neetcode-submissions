# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def dfs(node):
            if node is None:
                return 0
        
            left_h = 1 + dfs(node.left)
            right_h = 1 + dfs(node.right)

            return max(left_h, right_h)
        
        max_l = dfs(root.left)
        max_r = dfs(root.right)

        if abs(max_l - max_r) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        