# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        dict_nodes = collections.defaultdict(list)
        result = []
        queue = [(root, 0)]

        while queue:
            curr, col = queue.pop(0)
            dict_nodes[col].append(curr.val)

            if curr.left:
                queue.append((curr.left, col - 1))

            if curr.right:
                queue.append((curr.right, col + 1))

        for k in sorted(dict_nodes.keys()):
            result.append(dict_nodes[k])

        return result

  '''
T = O(N log N)
S = O(N)
  '''
