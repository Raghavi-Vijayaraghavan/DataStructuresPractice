class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
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
    listHead = None
    lL = LinkedList()
    for i in range(len(a)):
        listHead = lL.push(a[i])
    return listHead

def displayHead(head):
    temp = head
    while temp.next:
        print(temp.value)
        temp = temp.next
    print(temp.value)

displayHead(createAndUpdateHead([1,2,3,4]))

