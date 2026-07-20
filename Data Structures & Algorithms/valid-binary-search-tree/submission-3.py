# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #dfs
        def valid(node, val_range):
            if not node:
                return True

            if not (val_range[0] < node.val < val_range[1]):
                return False
            
            return valid(node.left, (val_range[0],node.val)) and valid(node.right, (node.val, val_range[1]))
        
        return valid(root, (-float('inf'), float('inf')))

