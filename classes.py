class input_no:
  def __init__(self):
    self.a=int(input("Enter the first number: "))
    self.b=int(input("Enter the second number:"))

class add:
  def __init__(self):
    x=input_no()
    self.sum= x.a+x.b
  def __str__(self):
    return str(self.sum)
   
class subtracti:
  def __init__(self):
    x=input_no()
    self.sum= str(x.a-x.b)
  def __str__(self):
    return str(self.sum)

class choice:
  def __init__(self):
    sign=input("Enter the operation to be performed (+ or -): ")
    if sign == "+" :
      self.fin=add()
    elif sign == "-":
      self.fin=subtracti()
  
class display:
  def __init__(self):
    c=choice()
    print(f"The result of the operations: {c.fin}")
  
d=display()
