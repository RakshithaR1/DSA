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
    to_del = node(value)
    current = self.top
    while current:
        if current.next.value == to_del.value:
          
          if current.next.next == None:
              current.next = None
              return 
          current.next = current.next.next
          print("Node is removed from the list")
          current = current.next  
        if current.next is None:
         return
     
        
      
  def display(self):
    current = self.top
    while current:
      print(current.value,end= "->")
      current = current.next
    print("None") 
  
l = linkedlist()
l.insert(8)
l.insert(9)
l.insert(10)
l.display()
l.delete(10)
l.display()