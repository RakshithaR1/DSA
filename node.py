class node:
  def __init__(self,value):
    self.value = value
    self.next = None
    
class linkedlist:
  def __init__(self):
    self.top = None
  def insert(self,value):
    self.val = node(value)
    if self.top is None:
      self.top = self.val
    else:
      current = self.top
      while current.next:
        current = current.next
      current.next = self.val
      
  def delete(self,value):
    if not self.top:
      print("The list is empty")
    else:
      head = self.top
      if head.value == value:
        if head.next==None:
          head=None
        else:
          head=head.next
      else:
        curr = head
        while curr:
          if curr.next.value==value:
            curr.next = curr.next.next
            break
          if not curr.next:
            return 
          curr=curr.next
  def display(self):
    current = self.top
    while current:
      print(current.value,end= " ")
      current = current.next
  
l = linkedlist()
l.insert(8)
l.insert(9)
l.insert(10)
l.display()
l.delete(10)
l.display()