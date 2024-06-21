class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def createRoot(self, a):
        tempRoot = self.root
        tempRoot = self.addNodes(a, 0, len(a)-1, tempRoot)
        return self.root

    def addNodes(self, array, start, end, root):
        if end < start:
            return
        else:
            mid = (start + end)//2
            if not root:
                root = TreeNode(array[mid])
            root.left = self.addNodes(array, start, mid-1, root.left)
            root.right = self.addNodes(array, mid+1, end, root.right)
            return root

def displayTreePreOrder(root):
    if root:
        print(root.value, end='-->')
        displayTreePreOrder(root.left)
        displayTreePreOrder(root.right)


bst = BinarySearchTree()
displayTreePreOrder(bst.createRoot([1,2,3,4,5,6,7]))

root = TreeNode(5)
root.left = TreeNode()
    
