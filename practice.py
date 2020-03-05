#!/usr/bin/env python
#from Data_structures.stack import stack
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



def is_match(p1, p2): 
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False
def balanced(paren_string):
    s=Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
        
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


#print(balanced("[]][]]]"))

s= Stack()
def div_by_2(dec_num):
    
    while dec_num >0:
        remainder= dec_num %2
        s.push(remainder)
        dec_num =dec_num // 2

    bin_num= ""

    while not s.is_empty():
        bin_num+= str(s.pop()) 
    return bin_num

#print(div_by_2(242))


def reverse(stack, input_string):
    
    
    for i in range(len(input_string)):
        stack.push(input_string[i])
    
    rev_str = ""
    while not stack.is_empty():
        rev_str+= stack.pop()
    return rev_str
stack =Stack()
input_str="Hello"
print(reverse(stack, input_str))