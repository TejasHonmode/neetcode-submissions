# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs
        maxval = -float('inf')
        good = 0
        def dfs(node, maxval):
            nonlocal good
            if node.val >= maxval:
                good += 1
            maxval = max(maxval, node.val)
            
            if node.left:
                dfs(node.left, maxval)
            if node.right:
                dfs(node.right, maxval)
        
        dfs(root, maxval)

        return good
