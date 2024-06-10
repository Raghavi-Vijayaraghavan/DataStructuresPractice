class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLl(nodeObj):
    current = nodeObj
    count = 0
    while current.next:
        count += 1
        current = current.next

    lastNode = current
    i = count
    while i > 0:
        lastNode.next = prevNode(nodeObj, i)
        lastNode = lastNode.next
        i -= 1
    lastNode.next = None
    return current

    
    
def printListNodeValues(nodeObj):
    current = nodeObj
    while current.next:
        print(current.data, '-->')
        current = current.next
    print(current.data)


def prevNode(node, counter):
    if counter == 1:
        return node
    else:
        return prevNode(node.next, counter-1)


start = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

start.next = second
second.next = third
third.next = fourth

printListNodeValues(start)
printListNodeValues(reverseLl(start))





