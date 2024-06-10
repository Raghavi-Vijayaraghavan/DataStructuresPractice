class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def createAndUpdateHead(a):
    head = None
    for i in range(len(a)):
        head = insertArrayIntoLl(head, a[i])
    return head


def insertArrayIntoLl(head, data):
    node = Node(data)
    if head is None:
        head = node
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = node
    return head

def returnLastEqualNode(node):
    while node.next:
        if node.value != node.next.value:
            return node
        node = node.next
    else:
        return node

def mergeLists(head1, head2):
    if head2 is None:
        return head1

    else:
        if head1.value > head2.value:
            head1, head2 = head2, head1
        else:
            temp1 = head1
            temp2 = head2
            while temp1.next:
                while temp1.value <= temp2.value:
                    temp1 = returnLastEqualNode(temp1)
                    temp1 = temp1.next
        
                    head2 = temp1.next
                    temp1.next = temp2
                
            
            return mergeLists(head1, head2)

def displayLl(head):
    if head is None:
        print('Empty Node')
    else:
        temp = head
        while temp.next:
            print(temp.value)
            temp = temp.next
        print(temp.value)

displayLl(mergeLists(createAndUpdateHead([1,1,4,5]), createAndUpdateHead([2,3,3,6])))
        
