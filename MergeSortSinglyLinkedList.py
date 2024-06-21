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
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        return self.head

def createAndUpdateHead(a):
    head = None
    lL = LinkedList()
    for i in range(len(a)):
        head = lL.push(a[i])
    return head

def displayList(head):
    temp = head
    while temp.next:
        print(temp.value)
        temp = temp.next
    print(temp.value)


def msDivide(head):
    temp = head
    if not temp.next:
        return head
    else:
        fast, slow = temp.next, temp
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        rHead = slow.next
        slow.next = None
        lHead = temp
        lNode = msDivide(lHead)
        rNode = msDivide(rHead)
        return msMerge(lNode, rNode)

def msMerge(head1, head2):
    if not head1 or not head2:
        if not head1:
            return head2
        else:
            return head1
    else:
        displayList(head1)
        print('#####')
        displayList(head2)
        temp1, temp2 = head1, head2
        if temp1.value > temp2.value:
            temp1, temp2 = temp2, temp1
        while temp1.next and temp1.next.value <= temp2.value:
            temp1 = temp1.next
        head2 = temp1.next
        temp1.next = temp2
        return msMerge(head1, head2)
        

head = createAndUpdateHead([5,4,1,2,6])
displayList(msDivide(head))
