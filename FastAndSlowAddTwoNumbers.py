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
    temp = head
    while temp.next:
        print(temp.value)
        temp = temp.next
    print(temp.value)

def addTwoNumbers(a,b):
    sumLl = LinkedList()
    sumInteger = carry = 0
    while a is not None or b is not None:
        if a is None:
            sumInteger = b.value+carry
        elif b is None:
            sumInteger = a.value+carry
        else:
            sumInteger = a.value+b.value+carry
            if sumInteger >= 10:
                sumInteger %= 10
                carry = 1
            else:
                carry = 0
            sumHead = sumLl.push(sumInteger)
        a,b = a.next,b.next
    if carry > 0:
        sumHead = sumLl.push(carry)
    return sumHead
            

displayList(createAndUpdateHead([1,2,3,4]))
a = createAndUpdateHead([9,9,9])
b = createAndUpdateHead([9,9,9])
#displayList(a)
displayList(addTwoNumbers(a,b))

