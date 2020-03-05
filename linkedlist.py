class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head =None

    def append(self, data):
        new_node =Node(data)
        
        if self.head is None:
            self.head =new_node
            return

        last_node= self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next= new_node
    def print_list(self):
        curr_node =self.head
        while curr_node:
            print(curr_node.data)
            curr_node=curr_node.next
        
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next=self.head
        self.head=new_node
    
    def insert(self, prev_node, data):
        if not prev_node:
            print("Doesnt exist")
            return
        
        new_node= Node(data)
        new_node.next = prev_node.next
        prev_node.next =new_node
     
    def delete(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head= cur_node.next
            cur_node=None
        
        prev = None
        while cur_node and cur_node.data !=key:
            prev = cur_node
            cur_node = cur_node.next
            #print(cur_node.data)
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node =None
        #print(prev.data) 
    
    def delete_pos(self, pos):
        cur_node=self.head

        if pos == 0:
            self.head= cur_node.next
            cur_node=None
            return

        prev = None
        count =1
        while cur_node and count!= pos:
            prev= cur_node
            cur_node=cur_node.next
            count+=1

        if cur_node is None:
            return
        
        prev.next=cur_node.next
        cur_node=None
    
    def len(self):
        count =0
        cur_node= self.head
        while cur_node:
            count+=1
            cur_node=cur_node.next
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1+ self.len_recursive(node.next)
        
    def swap_nodes(self, key1, key2):
        if key1==key2:
            return 
        
        prev1=None
        cur1= self.head
        while cur1 and cur1.data!=key1:
            prev1= cur1
            cur1=cur1.next

        prev2=None
        cur2=self.head
        while cur2 and cur2.data!=key2:
            prev2=cur2
            cur2=cur2.next

        if not cur1 or not cur2:
            return 

        if prev1:
            prev1.next =cur2
        else:
            self.head=cur2

        if prev2:
            prev2.next =cur1
        else:
            self.head=cur1

        cur1.next, cur2.next=cur2.next, cur1.next


    def reverse(self):
        
        prev = None
        cur= self.head
        while cur:
            nxt =cur.next
            cur.next= prev
            prev=cur
            cur=nxt
        self.head =prev
   
    def merge_two(self, llist):
        p=self.head
        q= llist.head 
        s= None

        if not p:
            return q
        if not q: 
            return p

        if p and q: 
            if p.data<=q.data:
                s=p
                p= s.next
            
            else:
                s=q
                q =s.next
                
            
            while p and q:
                if p.data<=q.data:
                   s.next =p
                   s= p
                   p=s.next
                else:
                    s.next =q
                    s= q
                    q= s.next
            if not p:
                s.next= q
            if not q:
                s.next = p
                
             
    def remove_dup(self):
        cur = self.head
        prev = None
        dupe= dict()
             
        while cur:
            if cur.data in dupe:
                prev.next= cur.next
                cur = None
            else:
                dupe[cur.data]=1
                prev=cur   
            cur=prev.next
    
    def n_to_lastNode(self, n):
        length = self.len()
        cur = self.head
        while cur:
            if length==n:
                print(cur.data)
                return 
            length-=1
            cur= cur.next
        if cur is None:
            return 

    
    def rotate(self, k):
        
        p=self.head
        q= self.head
        prev= None
        count =0
        while p and count<k:
            prev=p
            p=p.next
            q=q.next
            count+=1     
        p = prev
        while q:
            prev =q
            q= q.next
        q= prev
        
        q.next =self.head
        self.head= p.next
        p.next =None
    def pallindrome(self):
        s=""
        cur =self.head
        while cur:
            s+= cur.data
            cur= cur.next
        return s== s[::-1]
    
    def move_tail(self):
        cur =self.head
        prev =None
        while cur.next:
            prev= cur
            cur =cur.next
        cur.next= self.head
        prev.next =None
        self.head = cur

          
            
        

llist = LinkedList()
llist.append("C")
llist.append("A")
llist.append("C")
llist.append("D")
#llist.print_list()
#print(llist.len())
#llist.insert(llist.head.next,"E")
#llist.swap_nodes("A","A")
#print(llist.len_recursive(llist.head))
#llist.delete("E")
#llist.delete_pos(0)
#llist.delete_pos(0)
llist1= LinkedList()
llist2 = LinkedList()
llist1.append("1")
llist1.append("5")
llist1.append("7")
llist1.append("9")
llist1.append("10")
llist2.append("2")
llist2.append("3")
llist2.append("4")
llist2.append("6")
llist2.append("8")
#llist1.merge_two(llist2)
#llist1.print_list()
#llist.remove_dup()
#llist.print_list()
llist.n_to_lastNode(2)
#llist.rotate(2)
#print(llist1.merge_two(llist2))
#llist.reverse()
#llist.print_list()  
#print(llist.pallindrome())
#llist.move_tail()
#llist.print_list()