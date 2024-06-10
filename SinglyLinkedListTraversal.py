class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse_ll(nodeObj):
    current = nodeObj
    counter = 0
    while current is not None:
       counter += 1
       current = current.next
    return counter
        
def insertHeadNode(oldHead, newHeadData):
    newHead = Node(newHeadData)
    newHead.next = oldHead
    return newHead.data

def insertTailNode(nodeObj, tailData):
    current = nodeObj
    while not current.next:
        newNode = Node(tailData)
        nodeObj.next = newNode
    return newNode.data, newNode.next




#Create Nodes
head = Node(1)
second = Node(2)
third = Node(3)

#Connect the Nodes
head.next = second
second.next = third

#Traverse the nodes
print(traverse_ll(head))
print(insertHeadNode(head, 0))
print(insertTailNode(head, 4))
