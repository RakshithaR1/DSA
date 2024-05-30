class node:
  def __init__(self,value):
    self.data=value
    self.next = None

n1=node(1)
n2=node(2)
n1.next=n2
current = n1
while current:
  print(current.data,end="->")
  current = current.next
print("None")