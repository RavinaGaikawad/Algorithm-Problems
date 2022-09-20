# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        queue = []
        depth = 1
        queue.append((root, depth))
        
        while queue:
            
            curr, d = queue.pop(0)
            
            if curr.left is None and curr.right is None:
                return d
            
            if curr.left:
                queue.append((curr.left, d+1))
                
            if curr.right:
                queue.append((curr.right, d+1))
                
        return depth
    
