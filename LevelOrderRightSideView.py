class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = self.right = None

def rightSideView(root):
    queue = []
    queue.append(root)
    values = []
    while queue:
        values.append(queue[-1].value)
        for _ in range(len(queue)):
            n = queue.pop(0)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
    print(values)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.left = TreeNode(8)


rightSideView(root)
