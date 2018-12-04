#9.8
class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data) 
       
    def bst_insert(top, data):
        if top is None:
           return Tree(data)
        if data < top.data:
           top.left = bst_insert(top.left, data)
        elif data > top.data:
           top.right = bst_insert(top.right, data)
        return top 

    def bst_max(top):
       if top.data == None:
          raise ValueError('Drzewo jest puste')
       if top.right == None:
          return top.data
       while(top.right):
          top = top.right
       return top.data

    def bst_min(top):
       if top.data == None:
          raise ValueError('Drzewo jest puste')
       if top.left == None:
          return top.data
       while(top.left is not None):
          top = top.left
       return top.data


     root = Tree(5)
     root = bst_insert(root,5)
     root = bst_insert(root, 2)
     root = bst_insert(root, 7)
     root = bst_insert(root, 1)
     root = bst_insert(root, 10)
     print(bst_min(root))
     print(bst_max(root))
 


