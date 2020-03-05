"""#Stack data structure

D

C
B
A

----"""

class Stack():
    def __init__(self):
        self.items= []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == [] 
    
    def top(self):
        if not self.items.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items


s= Stack()
s.push("A")
s.push("B")
print(s.pop())
#print(s.get_stack())
#print(s.is_empty())
#s.pop()
#s.is_empty()