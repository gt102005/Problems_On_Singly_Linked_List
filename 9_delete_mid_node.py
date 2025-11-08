class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_List(object):
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
    
    def dispaly(self):
        current=self.head
        while current:
            print(">>",current.data,end="")
            current=current.next
        print()

# Two Pointer approach 
    def Remove_mid(self):
        slow=self.head
        fast=self.head
        previous=None
        while fast and fast.next is not None:
            previous=slow
            slow=slow.next
            fast=fast.next.next
        previous.next=slow.next

        

arr=[1,2,3,4,5,6,7,8,9,0,11,22,33,44,55,66,77,88,99,00]
links=Linked_List()
for i  in arr:
    links.Insert(i)
links.dispaly()
links.Remove_mid()
links.dispaly()

