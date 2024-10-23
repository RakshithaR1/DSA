
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if not node.right:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
        else:
            return 
            
    def preorder(self,node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)
        else:
            return
    
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)
        else:
            return 




t1 = Tree()
t1.insert(20)
t1.insert(10)
t1.insert(11)
t1.insert(4)
t1.insert(3)
t1.inorder(t1.root) 
# Inorder traversals are used in BSTs (Binary search trees) since they return the tree in the ascending order 
print()
t1.preorder(t1.root)
print()
t1.postorder(t1.root)
print()

# Preorder and postorder are less frequently used in BSTs but are still valuable for copying and deletion of the trees
     