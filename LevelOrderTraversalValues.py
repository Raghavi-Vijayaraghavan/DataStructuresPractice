class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = self.right = None

def levelOrderValues(root):
    queue = []
    queue.append(root)
    allNodesValues = []
    while queue:
        values = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            values.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        allNodesValues.append(values)
    print(allNodesValues)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

levelOrderValues(root)        

    
