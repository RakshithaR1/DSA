class node:
    def __init__(self,value):
        self.data = value
        self.next = None
class stacks:
    def __init__(self):
        self.head = None
    def append(self,value):
        new_node=node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head=new_node
    def delete(self):
        if not self.head:
            print("The Stack is empty")
            return 
        else:
            self.head=self.head.next
    def print_li(self):
        curr = self.head
        if not self.head:
            print("The stack is empty")
            return 
        while curr:
            print(curr.data,end= " ")
            curr = curr.next
s = stacks()
s.append(3)
s.append(2)
s.append(1)
s.delete()
s.print_li()