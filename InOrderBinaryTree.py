class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


def leftNodeValue(nodeObject):
    if nodeObject:
        nodeVal = leftNodeValue(nodeObject.left)
        if nodeVal:
            print(nodeVal)
        return nodeObject.value
        
def rightNodeValue(nodeObject):
    if nodeObject:
        return rightNodeValue(nodeObject.right)



rootNode = Node(1)
rootNode.left = Node(2)
rootNode.right = Node(3)
rootNode.left.left = Node(5)
rootNode.left.right = Node(6)
rootNode.right.left = Node(7)

print(str(leftNodeValue(rootNode.left)) + '--> ')

