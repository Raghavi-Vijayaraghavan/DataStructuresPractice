class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def createAndUpdateHead(a):
    head = None
    for i in range(len(a)):
        head = insertNodesToList(head, a[i])
    return head


def insertNodesToList(head, data):
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


def removeNthNode(head, n):
    fast, slow = head, head
    for i in range(n):
        fast = fast.next
    if fast is None:
        head = head.next
    else:
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
    return head

#displayList(createAndUpdateHead([1,2,3,4]))
displayList(removeNthNode(createAndUpdateHead([1,2,3,4]), 4))

    
