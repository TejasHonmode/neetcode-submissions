# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node and subRoot and node.val == subRoot.val :
                    if self.sameTree(node, subRoot):
                        return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return False
    
    def sameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False