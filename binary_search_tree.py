class Node:
    def __init__(self, data=None):
        self.data= data
        self.left= None
        self.right= None
class BST:
    def __init__(self):
        self.root= None
    
    def insert(self, data):
        if self.root is None:
            self.root= Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):    
        if data< cur_node.data:
            if cur_node.left is None:
                cur_node.left= Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data> cur_node.data:
             if cur_node.right is None:
                cur_node.right = Node(data)
             else:
                 self._insert(data, cur_node.right)
        else: 
            print("value exists")
    
    def find(self, data):
        if self.root:
            isfound= self._find(data, self.root)
            if isfound:
                return True
            return False
        else: 
            return None
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data< cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
        return False
    arr=[]
    def common_ancestor(node1, node2):
            


bst= BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(10)
bst.insert(7)
print(bst.find(4)) 