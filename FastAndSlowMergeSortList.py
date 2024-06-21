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
    head = None
    lL = LinkedList()
    for i in range(len(a)):
        head = lL.push(a[i])
    return head

def displayList(head):
    if head:
        temp = head
        while temp.next:
            print(temp.value)
            temp = temp.next
        print(temp.value)

def msDivide(head):
    temp = head
    if temp.next is None:
        return temp
    else:
        fast, slow = temp.next, temp
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        rNode = slow.next
        slow.next = None
        lNode = temp
        lHead = msDivide(lNode)
        rHead = msDivide(rNode)
        return msMerge(lHead,rHead)
def msMerge(l,r):
    if l and r:
        dummyNode = Node(0)
        tempNode = dummyNode
        while l and r:
            #displayList(l)
            #displayList(r)
            if l.value <= r.value:
                tempNode.next = l
                l = l.next
                if l:
                    l.next = None
            else:
                tempNode.next = r
                r = r.next
                if r:
                    r.next = None
        while l:
            tempNode.next = l
            l = l.next
            if l:
                l.next = None
        while r:
            tempNode.next = r
            r = r.next
            if r:
                r.next = None
        return dummyNode.next

testHead = createAndUpdateHead([5,3,8,1,2,7])
displayList(msDivide(testHead))
