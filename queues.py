class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class queue:
    def __init__(self):
        self.head=None
    def append(self,value):
        new_node=node(value)
        if not self.head:
            self.head=new_node
        else:
            curr = self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node
    def delete(self):
        if not self.head:
            print("The queue is empty.")
        else:
            self.head=self.head.next
    def print_queue(self):
        curr = self.head
        if not self.head:
            print("The queue is empty.")
            return 
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
q = queue()
q.append(1)
q.append(1)
q.append(2)
q.append(3)
q.delete()
q.print_queue()

        