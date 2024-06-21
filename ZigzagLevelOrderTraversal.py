class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = self.right = None


def zigzagNodes(root):
    queue = []
    queue.append(root)
    allNodesValues = []
    level = 1
    while queue:
        values = []
        queue = queue[::-1]
        for _ in range(len(queue)):
            node = queue.pop(0)
            values.append(node.value)
            if not level%2:
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        allNodesValues.append(values)
        level+=1
    print(allNodesValues)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.right.right.right = TreeNode(9)

zigzagNodes(root)
