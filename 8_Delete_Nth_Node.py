# The problem states that the Nth node to be remove from the back side 
class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class Links(object):
    def __init__(self):
        self.head=None

    def Insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        current=self.head
        while current and current.next is not None:
            current=current.next
        current.next=new_node

    def DeleteNode(self,position):
        slow=self.head
        fast=self.head
        for i in range(position):
            fast=fast.next
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        print("----Deleted successfully----")

        
    
    def Display(self):
        current=self.head
        while current:
            print(">>",current.data,end="")
            current=current.next
        print()

arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
links=Links()
for i in arr:
    links.Insert(i)
links.Display()
links.DeleteNode(4)
links.Display()
    