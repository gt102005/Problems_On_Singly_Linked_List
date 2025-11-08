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
    
    def Check_Loop_Starting_Position(self):
        current=self.head
        dict_=dict()
        count=1
        while current and current.next is not None:
            if current not in dict_:
                dict_[current]=count
                count+=1
                current=current.next
            else:
                return dict_[current]
            
            



    def Dispaly(self):
        current=self.head
        while current:
            print(">>",current.data,end="")
            current=current.next
        print()

arr=[10,20,30,40,50,60,70,80,90]
links=Links()
l1=links.Insert(arr[0])
l2=links.Insert(arr[1])
l3=links.Insert(arr[2])
l4=links.Insert(arr[3])
l5=links.Insert(arr[4])
l6=links.Insert(arr[5])
l7=links.Insert(arr[6])
l8=links.Insert(arr[7])
l9=links.Insert(arr[8])
links.Dispaly()
links.Loop(45,l5)
# links.Dispaly()
print(links.Check_Loop_Starting_Position())
