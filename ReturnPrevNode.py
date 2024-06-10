class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insertArrayToLl(a):
    head = None
    for i in range(len(a)):
        head = createAndUpdateHead(head, a[i])
    return head


def createAndUpdateHead(head, data):
    node = Node(data)
    if head is None:
        head = node
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = node
    return head
    
def displayLl(head):
    temp = head
    while temp.next:
        print(temp.value)
        temp = temp.next
    print(temp.value)

def returnPrevNode(head,count):
    if count == 1:
        return head
    else:
        return returnPrevNode(head.next, count-1)


#displayLl(insertArrayToLl([1,2,3,4,5,6]))
displayLl(returnPrevNode(insertArrayToLl([1,2,3,4,5,6]), 3))
    
