
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    # Base Case
    if root is None:
        return
     
    # Create an empty queue
    # for level order traversal
    queue = []
 
    # Enqueue Root and initialize height
    queue.append(root)
 
    while(len(queue) > 0):
       
        # Print front of queue and
        # remove it from queue
        print (queue[0].val, end=' ')
        node = queue.pop(0)
 
        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
    
    
#Creating Tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)


print('bfs')
bfs(root)


'''
BFS
Time Complexity = O(N)
Space Complexity = O(W) where W = width of the tree
'''


        
    
