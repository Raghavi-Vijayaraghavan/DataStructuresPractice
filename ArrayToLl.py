class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def createHeadNode(a):
    head = None
    for i in range(len(a)):
        head = insertToLl(head, a[i])
    return head


def insertToLl(head, data):
    node = Node(data)
    if head is None:
        head = node
    else:
        if head.next is None:
            head.next = node
        else:
            temp = head.next
            while temp.next:
                temp = temp.next
            temp.next = node
    return head

def displayLl(head):
    print(head.value)
    while head.next is not None:
        temp = head.next
        print(temp.value)
        temp = temp.next
    print(temp.value)

displayLl(createHeadNode([1,2,3,4,5]))
