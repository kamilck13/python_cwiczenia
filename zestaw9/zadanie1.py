#9.1
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def printList(node):
    while node:
        print(node)
        node = node.next
    print("-----------")


def remove_head(node):
    if node == None:
        raise ValueError("Lista jest pusta")
    if node.next == None:
        return None, node.data
    return node.next, node.data

def remove_tail(node):
    if node == None:
        raise ValueError("Lista jest pusta")
    last = None
    head = node
    while node.next:
        last = node
        node = node.next
    if last == None:
        return None, node.data
    last.next = None
    return head, node.data
    
print('test delete tail')
head = None
head = Node(1, head)
head = Node(2, head)
head = Node(3, head)
printList(head)
head, data = remove_tail(head)
printList(head)
head, data = remove_tail(head)
printList(head)
head, data = remove_tail(head)
printList(head)
# head, data = remove_tail(head)

print('test delete head')
head = None
head = Node(1, head)
head = Node(2, head)
head = Node(3, head)
printList(head)
head, data = remove_head(head)
printList(head)
head, data = remove_head(head)
printList(head)
head, data = remove_head(head)
printList(head)
# head, data = remove_head(head)
