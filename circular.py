class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularlinkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=node(data)
        if not self.head:
            self.head=new_node
            new_node.next=self.head
        else:
            curr = self.head
            while curr.next!=self.head:
                curr = curr.next
            curr.next=new_node
            new_node.next=self.head
    def delete_node(self,data):
        if not self.head:
            print("The list is empty")
            return 
        curr=self.head
        prev=None
        while True:
            if curr.data==data:
                if prev:
                    prev.next=curr.next
                else:
                    while curr.next!=self.head:
                        curr=curr.next
                    if self.head==self.head.next:
                        self.head=None
                    else:
                        curr.next=self.head.next
                        self.head=self.head.next
                return 
            prev=curr
            curr=curr.next
            if curr==self.head:
                break 
    def print_li(self):
        curr=self.head
        if not curr:
            print("list is empty")
            return 
        while True:
            print(curr.data,end=" ")
            curr=curr.next
            if curr==self.head:
                break
cll = circularlinkedlist()
# cll.append(1)
# cll.append(2)
cll.append(3)
cll.delete_node(3)
cll.print_li()