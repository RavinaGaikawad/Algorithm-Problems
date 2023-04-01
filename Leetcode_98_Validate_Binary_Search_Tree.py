# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def isValidBinaryTree(root, left, right):

            if not root:
                return True

            if root.val <= left or root.val >= right:
                return False

            return (isValidBinaryTree(root.left, left, root.val) and isValidBinaryTree(root.right, root.val, right))

        return isValidBinaryTree(root, float('-inf'), float('inf'))
      
      '''
        T = O(N)
        S = O(N)
      '''
      
