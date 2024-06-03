# class input_no:
#   def __init__(self):
#     self.a=int(input("Enter the first number: "))
#     self.b=int(input("Enter the second number:"))
# a=input_no()
# print(a.a,a.b)
# c=str(1+2)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of Person
p = Person("Alice", 30)

# Printing the instance
print(p)  # Output: <__main__.Person object at 0x7f9d9d6f4a90>

