class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doublylinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        new_node=node(data)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
    def prepend(self,data):
        new_node=node(data)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
    def delete(self,data):
        if not self.head:
            print("The list is empty")
            return
        if self.head.data==data:
            self.head=self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail=None
        else:
            curr = self.head
            pre=None
            while curr and curr.data!=data:
                pre=curr
                curr=curr.next
            pre.next=curr.next
            if curr.next:
                curr.next.prev=pre
            else:
                self.tail=pre
    def print_li(self):
        curr = self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next

dll = doublylinkedlist()
dll.append(2)
dll.prepend(1)
dll.append(3)
dll.append(4)
dll.delete(4)
dll.print_li()   