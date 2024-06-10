class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def createAndUpdateHead(a):
    head = None
    for i in range(len(a)):
        head = insertNodesToLl(head, a[i])
    displayLl(head)

def insertNodesToLl(head, data):
    node = Node(data)
    if head is None:
        head = node
    else:
        tempNode = head
        while tempNode.next is not None:
            tempNode = tempNode.next
        tempNode.next = node
    return head

def displayLl(head):
    tempNode = head
    while tempNode.next is not None:
        print(tempNode.value)
        tempNode = tempNode.next
    print(tempNode.value)


createAndUpdateHead([1,2,3,4])



        
