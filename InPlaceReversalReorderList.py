class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return self.head

def createAndUpdateHead(a):
    lL = LinkedList()
    head = None
    for i in range(len(a)):
        head = lL.push(a[i])
    return head

def displayHead(head):
    temp = head
    while temp.next:
        print(temp.value)
        temp = temp.next
    print(temp.value)

def reverseHead(head):
    previous, placeholder = None, None
    while head:
        placeholder = head.next
        head.next = previous
        previous = head
        head = placeholder
    return previous

def reorderList(head):
    temp = head
    while temp.next:
        temp.next = reverseHead(temp.next)
        temp = temp.next
    return head

displayHead(reorderList(createAndUpdateHead([5,4,3,2,1])))
