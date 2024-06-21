class TreeNode:
    def __init__ (self, data):
        self.value = data
        self.left = self.right = None

def minimumDepthOfTree(root):
    queue = []
    queue.append(root)
    count = 1 if root else 0
    while queue:
        node = queue.pop(0)
        if node.left or node.right:
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            break
    print('Min Depth ', count)


root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)

minimumDepthOfTree(root)
