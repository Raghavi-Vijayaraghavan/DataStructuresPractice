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
    head = None
    lL = LinkedList()
    for i in range(len(a)):
        head = lL.push(a[i])
    return head

def displayHead(head):
    while head.next:
        print(head.value)
        head = head.next
    print(head.value)

def reverseHead(head):
    current = head
    prev, nextNode = None, None
    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev

def splitList(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    node2 = slow.next
    slow.next = None
    node1 = head
    return node1, node2

def mergeAndReorder(node1, node2):
    dummyNode = Node(0)
    temp = dummyNode
    node2 = reverseHead(node2)
    while node1 or node2:
        if node1:
            temp.next = node1
            temp = temp.next
            node1 = node1.next
        if node2:
            temp.next = node2
            temp = temp.next
            node2 = node2.next
    return dummyNode.next

#displayHead(reverseHead(createAndUpdateHead([5,4,3,2,1])))
head1, head2 = splitList(createAndUpdateHead([6,5,4,3,2,1]))
displayHead(head1)
print('#####')
displayHead(head2)
#displayHead(mergeAndReorder(head1, head2))
            
    
        
