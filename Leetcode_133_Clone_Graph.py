"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        dict_nodes = {}
        head = Node(node.val)
        dict_nodes[node.val] = head           

        queue = [node]

        while queue:
            curr = queue.pop(0)

            for neighbor in curr.neighbors:
                if neighbor.val not in dict_nodes:
                    dict_nodes[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                dict_nodes[curr.val].neighbors.append(dict_nodes[neighbor.val])

        return head

'''
    T = O(N)
    S = O(N)
'''
