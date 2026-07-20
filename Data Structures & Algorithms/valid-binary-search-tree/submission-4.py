# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #bfs

        q = deque([[root, (-float('inf'), float('inf'))]])
        while q:
            node, v_range = q.popleft()
            if not v_range[0] < node.val < v_range[1]:
                return False
            
            if node.left:
                q.append([node.left, (v_range[0], node.val)])
            if node.right:
                q.append([node.right, (node.val, v_range[1])])
        
        return True