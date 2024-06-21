class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = self.right = None

def displayTreePreOrder(root):
    if root:
        print(root.value, end = '-->')
        displayTreePreOrder(root.left)
        displayTreePreOrder(root.right)


def averageOfLevels(root):
    queue = []
    queue.append(root)
    res = []
    while queue:
        Sum = count = 0
        for _ in range(len(queue)):
            node = queue.pop(0)
            Sum += node.value
            count+=1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(Sum/count)
    print(res)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.right = TreeNode(9)
root.left.left = TreeNode(11)
root.right.right = TreeNode(20)
averageOfLevels(root)
                
