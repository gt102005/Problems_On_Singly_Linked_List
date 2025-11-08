# The problem statement is to remove the nodes in the linked list if the higher value node present in the right of the linked list 

class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
class Connect(object):
    def __init__(self):
        self.head=None
    
    def add(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return 
        current=self.head
        while current and current.next is not None:
            current=current.next
        current.next=newnode

    def display(self):
        current=self.head
        while current:
            print(" >> ",current.data,end="")
            current=current.next
        print()

    def remove_node(self):
        

   
        
        cc=dummy_node
        while cc:
            print(" >> ",cc.data,end="")
            cc=cc.next
        print()

   
        

    
connect=Connect()
connect.add(5)
connect.add(3)
connect.add(13)
connect.add(3)
connect.add(8)
connect.display()
connect.remove_node()

