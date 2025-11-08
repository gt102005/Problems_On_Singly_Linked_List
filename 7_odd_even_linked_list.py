class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class Links:
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

# Way to sort the linked list properly and join the pointer nodes 
    def Odd_Even(self):
        if self.head is None:
            return "No Node "
        oddptr=odd=self.head
        evenptr=even=self.head.next
        while even and even.next is not None:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenptr

        while oddptr is not None:
            print("-->>",oddptr.data,end="")
            oddptr=oddptr.next
        print()

    
    def Dispaly(self):
        current=self.head
        while current:
            print("->>",current.data,end="")
            current=current.next
        print()

arr=[1,2,3,4,5,6,7,8,9,0,1,11,22,33,44,55,66,77,88,99,100]
links=Links()
for i in arr:
    links.Insert(i)
links.Dispaly()
links.Odd_Even()