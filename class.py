class a:
     b=10

x=a()
y=a()
print(f" {x.b} {y.b}")#The same attributes are being accessed 
x.b=20 #A new attribute is being assigned for the instance of x
print(f" {x.b} {y.b}") #The updated instances are being displayed that is 20 and 10

class attributes:
  def __init__(self,name,age):
    self.name=name
    self.age=age
a = attributes("Ray",18)
print(a.name)#Attributes are created within the class and they are used to represent data related with the instances within the class

class method:
  def example():
    print("This method is accessed.")
m=method
m.example()#methods are functions within the class that have a specific task to execute

class dog:
  def __init__(self):
    self.sound="woof"
    print(self.sound)
d=dog()#A constructor is used to initialize an object as soon as it is created .'__init__' is a constructor created in a class


class animal:
  def method():
    print("This is an animal")
class cat(animal):
  def c():
    print("This is a cat.")
c = cat
c.method()#here the cat class is the child class and animal is the parent class from which method() function is inherited and can 
          #be accessed by the instance of the class cat


class account:
  def __init__(self):
    self.__money=1000
  
  def get_balance(self):
    print(self.__money)
x=account()
x.get_balance() #__money cannot be directly accessed since encapsulation restricts the direct access

class polymorphism:
  def sound():
    print("Random sound")
class cow(polymorphism):
  def sound():
    print("Moo")
class lion(polymorphism):
  def sound():
    print("Roar")
c=cow
l=lion
c.sound()#here the function sound exists in two forms in both the sub classes cow and lion and are getting accessed 
l.sound()


#The same example given above can also be used to explain overriding where the subclass is allowed to override a specific implementation
#in the parent class

class circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return self.pi * self.radius * self.radius
circle1 = circle(5)
print(circle1.calculate_area()) #class variables are variables that can be accessed by all methods and instances in the class
#in the above example pi is called as a clas variable


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 6)
print(rectangle1.calculate_area()) #instance variables are the variables which are unique among each instance 
print(rectangle2.calculate_area())  #here 4,5 and 3,6 are called as instance variable

class destructors:
  def __del__(self):
    print("Object is destroyed")
d=destructors()
del d #Destructors are called automatically when the execution of the program is done 

