class input_no:
  def __init__(self):
    self.a=int(input("Enter the first number: "))
    self.b=int(input("Enter the second number:"))

class add:
  def __init__(self):
    x=input_no()
    self.sum= str(x.a+x.b)
   
class subtracti:
  def __init__(self):
    x=input_no()
    self.sum= str(x.a-x.b)

class choice:
  def __init__(self):
    sign=input("Enter the operation to be performed (+ or -): ")
    if sign == "+" :
      self.fin=str(add())
    elif sign == "-":
      self.fin=str(subtracti())
  
class display:
  def __init__(self):
    c=choice()
    print(f"The result of the numbers {str(c.fin)}")
  
d=display()
