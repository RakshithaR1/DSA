# # class input_no:
# #   def __init__(self):
# #     self.a=int(input("Enter the first number: "))
# #     self.b=int(input("Enter the second number:"))
# # a=input_no()
# # print(a.a,a.b)
# # c=str(1+2)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # Creating an instance of Person
# p = Person("Alice", 30)
# print(p.name)
# print(p)
# # Printing the instance
#  # Output: <__main__.Person object at 0x7f9d9d6f4a90>

class node:
    def __init__(self,data):
        self.data= data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    def prepend(self,data):
        new_node =node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def dele(self,data):
        if not self.head:
            print("The list is empty")
            return
        if self.head.next is None:
                self.head = None
        else:
            curr = self.head
            if self.head.data == data:
                self.head = self.head.next
            else:
                curr = self.head
                prev = None
                while curr.next is not None:
                    if curr.data == data:
                        prev.next = curr.next 
                        return
                    prev = curr
                    curr = curr.next
                print("The key does not exist")
    def traverse(self):
        if not self.head:
            print("The list is empty.")
            return 
        curr = self.head
        while curr:
            print(curr.data,end = " ")
            curr= curr.next
l =linkedlist()


l.traverse()
l.dele(1)
l.traverse()

                    
                          
                    
                         



        