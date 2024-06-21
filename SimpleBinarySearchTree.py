class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.addNode(self.root, data)
        return self.root

    def addNode(self, root, data):
        if root.value > data:
            if not root.left:
                root.left = TreeNode(data)
            else:
                self.addNode(root.left, data)
        else:
            if not root.right:
                root.right = TreeNode(data)
            else:
                self.addNode(root.right, data)


def displayTreeInOrder(root):
    if root:
        displayTreeInOrder(root.left)
        print(root.value, end = '->')
        displayTreeInOrder(root.right)
    

def createAndUpdateRoot(a):
    root = None
    bst = BinarySearchTree()
    for i in range(len(a)):
        root = bst.add(a[i])
    return root


displayTreeInOrder(createAndUpdateRoot([10,3,5,12]))
