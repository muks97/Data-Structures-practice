class Stack(object):
    def __init__(self):
        self.items=[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
       if len(self.items)==0:
           return True
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items) 
    def __len__(self):
        return self.size()     

class Queue(object):                              
   def __init__(self):
    self.items=[]
   
   def enqueue(self, item):
        self.items.insert(0, item)
   def dequeue(self):
       if not self.is_empty():
        return self.items.pop()
   def is_empty(self):
       if len(self.items)==0:
           return True
   def peek(self):
       if not self.is_empty():
           return self.items[-1].value
   def __len__(self):
        return self.size()
   def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value):
        self.value= value
        self.left = None
        self.right= None

class Binary_Tree(object):
      def __init__(self, root):  
          self.root = Node(root)
        
      def print_tree(self, type):
          if type=="preorder":
              return self.preorder(tree.root, "")
          elif type=="postorder":
              return self.postorder(tree.root, "")
          elif type=="inorder":
              return self.inorder(tree.root, "")
          elif type =="levelorder":
              return self.levelorder(tree.root)
          elif type =="reverse levelorder":
              return self.reverse_levelorder(tree.root)   
              
      def preorder(self, start, traversal):
          if start:
              traversal+= (str(start.value)+ "-")
              traversal = self.preorder(start.left, traversal)
              traversal= self.preorder(start.right, traversal)
          return traversal 
      
      def postorder(self, start, traversal1):
           if start:
                traversal1= self.postorder(start.left, traversal1)
                traversal1= self.postorder(start.right, traversal1)
                traversal1+= (str(start.value)+ "-") 
           return traversal1

      def inorder(self, start, traversal):
           if start:
               traversal = self.inorder(start.left, traversal)
               traversal+= (str(start.value)+ "-")
               traversal= self.inorder(start.right, traversal)
           return traversal 
      def levelorder(self, start):
           if start is None:
               return 
           queue = Queue()
           queue.enqueue(start)

           traversal = ""
           while len(queue)> 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

           return traversal
      def reverse_levelorder(self, start):       
          stack= Stack()
          queue= Queue()   
          if start is None:
            return 
          traversal=""
          queue.enqueue(start)
          while len(queue)>0:
              node = queue.dequeue()
              stack.push(node)

              if node.left:
                  queue.enqueue(node.left)
              if node.right:
                  queue.enqueue(node.right)
                
          while len(stack)>0:
              node =stack.pop()
              traversal+=str(node.value)+ "-"
            
          return traversal
      def height(self, node):
          if node is None:
              return -1
          left_height= self.height(node.left)
          right_height = self.height(node.right)

          return 1 + max(left_height, right_height)    
      def common_ancestor(self, node1):
         path = tree.levelorder(tree.root)
         for i in path:
            if i ==node1:


tree= Binary_Tree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
tree.common_ancestor(3)
#print(tree.height(tree.root))
#print(tree.print_tree("levelorder"))
