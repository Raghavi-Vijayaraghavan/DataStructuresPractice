class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insertArrayToLl(a):
    head = None
    for i in range(len(a)):
        head = createAndUpdateHead(head, a[i])
    return head

def createAndUpdateHead(headNode, data):
    node = Node(data)
    if headNode == None:
        headNode = node
    else:
        temp = headNode
        while temp.next:
            temp = temp.next
        temp.next = node
    return headNode

def reverseHead(head):
    temp = head
    listLength = 0
    while temp.next:
        temp = temp.next
        listLength += 1
    lastNode = temp
    for i in range(listLength, 0, -1):
        lastNode.next = returnPreviousNode(head, i)
        lastNode = lastNode.next
    lastNode.next = None
    return temp

def returnPreviousNode(headNode, counter):
    if counter == 1:
        return headNode
    else:
        return returnPreviousNode(headNode.next, counter-1)

def displayLl(head):
    while head.next:
        print(head.value)
        head = head.next
    print(head.value)

def isPalindrome(head):
    reversedHead = reverseHead(head)
    isPalin = True
    while head.next:
        if head.value == reversedHead.value:
            head = head.next
            reversedHead = reversedHead.next
        else:
            isPalin = False
            break
    if head.value != reversedHead.value:
        isPalin = False
    print(isPalin)
    
isPalindrome(insertArrayToLl([1,2,3,2,1]))
