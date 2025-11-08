class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
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
        return new_node
    def Loop(self,data,node):
        new_node=Node(data,node)
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node

# this is the first way to check the loop in the linked list 
    def CheckLoop(self):
        current=self.head
        list_=list()
        while current and current.next is not None:
            if current in  list_:
                return "Loop Detected"
            else:
                list_.append(current)
                current=current.next
        return "Loop Not Detected"

# this is the second way to check the loop in the linked list 
    def CheckLoop_Using_Pointer(self):
        current=self.head
        slow=self.head
        if self.head is None:
            return False
        else:
            fast=self.head.next
        while fast and fast.next is not None:
            if fast==slow:
                return "Loop Detected"
            else:
                slow=slow.next
                fast=fast.next.next
        return "Loop Not Detected"


    def Dispaly(self):
        current=self.head
        while current:
            print(">>",current.data,end="")
            current=current.next
        print()

arr=[10,20,30,40,50,60,70,80,90]
links=Links()
l0=links.Insert(arr[0])
l1=links.Insert(arr[1])
l2=links.Insert(arr[2])
l3=links.Insert(arr[3])
l4=links.Insert(arr[4])
l5=links.Insert(arr[5])
l6=links.Insert(arr[6])
l7=links.Insert(arr[7])
l8=links.Insert(arr[8])
links.Dispaly()
links.Loop(55,l4)
# links.Dispaly()
print(links.CheckLoop())
print(links.CheckLoop_Using_Pointer())