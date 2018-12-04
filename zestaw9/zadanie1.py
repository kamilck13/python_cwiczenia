#9.1
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def remove_head(node):
       if node.data == None:
          raise ValueError("Lista jest pusta")
       return node.next, node.next.data

    def remove_tail(node):
       if node.data == None:
          raise ValueError("Lista jest pusta")
       last = None
       head = node
       while node.next:
          last = node
          node = node.next
       if last == None:
          return Node(None), None
          last.next = None
       return head, head.data

    def printList(node):
        while node:
           print(node)
           node = node.next
        print("-----------")

    head = None
    head = Node(1, head)
    head = Node(2, head)
    printList(head)
    head, data = remove_tail(head)
    printList(head)
    head, data = remove_tail(head)
    printList(head)
    head, data = remove_tail(head)
