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
    
    def Reverse(self):
        previous=None
        temp=self.head
        while temp is not None:
            front=temp.next
            temp.next=previous
            previous=temp
            temp=front
        
        while previous:
            print(" -->> ",previous.data,end="")
            previous=previous.next
        print()


        



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
link.Reverse()

