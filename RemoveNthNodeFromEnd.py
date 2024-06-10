class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def createAndUpdateHead(a):
    head = None
    for i in range(len(a)):
        head = insertElementsIntoList(head, a[i])
    return head

def insertElementsIntoList(head, data):
    node = Node(data)
    if head is None:
        head = node
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = node
    return head

def displayList(head):
    temp = head
    while temp.next:
        print(temp.value)
        temp = temp.next
    print(temp.value)

def removeNode(head, nodeNumber):
    temp = head
    listLength = 0
    while temp.next:
        temp = temp.next
        listLength += 1
    nodePosition = listLength-(nodeNumber-1)
    prevNode = findPrevNode(head, nodePosition)
    currentNode = findCurrentNode(head, nodePosition)
    prevNode.next = currentNode.next
    currentNode.next = None
    return head
    
    
def findPrevNode(headNode, nodePosition):
    if nodePosition == 1:
        return headNode
    else:
        return findPrevNode(headNode.next, nodePosition-1)

def findCurrentNode(headNode, nodePosition):
    for i in range(nodePosition):
        headNode = headNode.next
    return headNode

displayList(createAndUpdateHead([1,2,3,4,5,6]))
displayList(removeNode(createAndUpdateHead([1,2,3,4,5,6]), 2))


  
    
        
    
    
