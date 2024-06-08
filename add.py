def get_two_numbers():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    return a,b

def add_two_numbers(a,b):
    pass

def show_results(a,b,sum):
   print(f"{a}+{b}={sum}")

a,b=get_two_numbers()
sum = add_two_numbers(a,b)
show_results(a,b,sum)