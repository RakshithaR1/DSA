class node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
class hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
    def hash_function(self,key):
        return hash(key)%self.size
    def insert_(self,key,value):
        index = self.hash_function(key)
        new_node = node(key,value)
        if not self.table[index]:
            self.table[index]=new_node
        else:
            curr = self.table[index]
            while curr is not None:
                if curr.key ==key:
                    new_node.next = curr.next
                    curr.next = new_node
                    return 
                if curr.next is None:
                    curr.next = new_node
                    return 
                curr = curr.next
           
    def print_hash(self,key):
        index = self.hash_function(key)
        curr = self.table[index]
        while curr is not None:
            if curr.key == key:
                values = []
                while curr is not None:
                    if curr.key == key:
                        values.append(curr.value)
                    curr=curr.next
                print(values)
                return
            curr = curr.next
    def delete(self,key):
        index = self.hash_function(key)
        curr = self.table[index]
        prev =None
        while curr is not None:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    curr = curr.next
            else:
                prev = curr 
                curr = curr.next
            
h = hashtable(10)
h.insert_("Bob",3)
h.insert_("Bob",4)
h.insert_("Eve",5)
h.print_hash("Bob")

                

