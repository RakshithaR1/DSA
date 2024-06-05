class Node:
  def __init__(self,value):
    self.data=value
    self.next=None
  def add_node(self,a,value):
    current=Node(value)
    head =a
    if head.next is None:
      head.next=current
    else:
      c=a
      while c.next is not None:
        c=c.next
      c.next=current
      
      
a=Node("srini")
a.delete_node("srini")

current = a
while current:
  print(current.data)
  current=current.next

      
    
    