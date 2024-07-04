class TreeNode:
    def __init__(self,data):
        self.value = data
        self.left = self.right = None


allPaths = []
paths = []
def binaryTreePaths(root):
    if root is None:
        return
    paths.append(root.value)
    if root.left is None and root.right is None:
        allPaths.append(paths)
        
    else:
        binaryTreePaths(root.left)
        binaryTreePaths(root.right)
    paths.pop(-1)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)

binaryTreePaths(root)
print(allPaths)

        
