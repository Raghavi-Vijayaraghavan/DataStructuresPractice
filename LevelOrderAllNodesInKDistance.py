class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = self.right = None

def getD(targetNode, root):
    queue = []
    queue.append(root)
    D = 0
    isTargetFound = False
    while queue and not isTargetFound:
        D += 1
        for _ in range(len(queue)):
            n = queue.pop(0)
            if n.value == targetNode.value:
                isTargetFound = True
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
            
        
