class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class postfix:
    def __init__(self):
        self.head = None
    def get_exp(self):
        self.expression = input("Enter the postfix expression: ")
    def evaluate(self):
        for i in self.expression:
            if i.isdigit():
                new_node=node(int(i))
                if not self.head:
                    self.head=new_node
                else:
                    new_node.next=self.head
                    self.head=new_node
            else:
                if not self.head and self.head.next:
                    print("No enough digits to calculate yet.")
                    continue
                if i == '+':
                    res = node(None)
                    res.data = self.head.data + self.head.next.data
                    res.next=self.head.next.next
                    self.head = res 
                elif i == '-':
                    res = node(None)
                    res.data = self.head.data - self.head.next.data
                    res.next=self.head.next.next
                    self.head = res
                elif i == '*':
                    res = node(None)
                    res.data = self.head.data * self.head.next.data
                    res.next=self.head.next.next
                    self.head = res
                elif i == '/':
                    res = node(None)
                    res.data = self.head.data / self.head.next.data
                    res.next=self.head.next.next
                    self.head = res
                else:
                    print(f"{i} is an invalid operation sign and has be skipped.")
    def output(self):
        print(f"The result of the expression {self.expression} = {self.head.data}")
p = postfix()
p.get_exp()
p.evaluate()
p.output()           