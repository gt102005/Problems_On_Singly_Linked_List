class Node(object):
    def __init__(self,data):
        self.next=None
        self.data=data
class Links(object):
    def __init__(self):
        self.head=None
    def Insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node
    def Display_mid(self):
        current=self.head
        slow=self.head
        fast=self.head
        while fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        print("Mid of the linked list is >>>",slow.data)


    def display(self):
        current=self.head
        while current:
            print("-->",current.data,end="")
            current=current.next
        print()
    
arr=[10,20,30,40,50,60,70,80,90]
link=Links()
for i in arr:
    link.Insert(i)
link.display()
link.Display_mid()

