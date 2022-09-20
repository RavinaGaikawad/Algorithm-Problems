#Tree definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):  
    # Base Case
    if not root:
        return

    dfs(root.left) # Go left
    print(root.val, end=' ') # Print root val
    dfs(root.right) # Go right
    
#Creating Tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)


print('dfs')
dfs(root)

'''
DFS
Time Complexity = O(N)
Space Complexity = O(H) where H = height of the tree
'''
