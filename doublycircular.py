class node:
    def __init__(self,value):
        self.data=value
        self.prev=None
        self.next=None

class doublyCircular:
    def __init__(self):
        self.head=None

    def append(self,value):
        new_node=node(value)
        if not self.head:
            self.head=new_node
            new_node.next = self.head
            self.head.prev=new_node
            
        else:
            curr=self.head.prev
            curr.next=new_node
            new_node.next  =self.head
            new_node.prev  = curr
            self.head.prev=new_node
              
    def print_li(self):
        curr = self.head
        if not curr:
            print("The list is empty")
            return
        while curr.next !=self.head:
            print(curr.data)
            curr  = curr.next
        print(curr.data)
    def prepend(self,data):
        new_node = node(data)
        if not self.head:
            self.head=  new_node
            new_node.prev =self.head
            self.head.next=new_node
        else:
            first = self.head
            last = self.head.prev
            self.head=new_node
            new_node.next=first
            new_node.prev=first.prev
            first.prev=new_node
            last.next=new_node
    def delete(self,data):
        if not self.head:
            print("The list is empty")
            return 
        first = self.head
        last = self.head.prev
        if first.data == data:
            if first == first.next:
                first =None
            else:
                last.next = first.next
                first.next.prev = first.prev
                self.head = first.next
        else:
            curr = first
            while curr.next != first and curr.data != data:
                curr = curr.next  
            curr.next.prev = curr.prev
            curr.prev.next = curr.next 

dll = doublyCircular()
dll.delete(1)
dll.print_li()