class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Links(object):
    def __init__(self):
        self.head=None
    
    def Insert(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            return 
        current=self.head
        while current and current.next is not None:
            current=current.next
        current.next=newNode

    def Show(self):
        current=self.head
        while current:
            print(">>",current.data,end="")
            current=current.next
        print()

    def Swap(self):
        current=self.head
        
            # current=front.next
        



arr=[11,22,33,44,55,66,77,88,99,111]
link=Links()
for i in arr:
    link.Insert(i)
link.Swap()
link.Show()
