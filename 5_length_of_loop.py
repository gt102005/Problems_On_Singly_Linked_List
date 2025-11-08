# Function to create a Node of the linked list 
class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class Links(object):
    def __init__(self):
        self.head=None

# Function to Insert each Node in the linked list 
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

# Function Loop to create a loop in the linked list
    def Loop(self,data,node):
        new_node=Node(data,node)
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node
    
    # this is the first approach to the problem statement - Finding the length of the loop in the  linked list  
    def Length_Of_Loop(self):
        print("First Method using the Dict method ---->", end="")
        current=self.head
        dict_=dict()
        count=1
        while current and current.next is not None:
            if current not in dict_:
                dict_[current]=count
                current=current.next
                count=count+1
            else:
                return count-dict_[current]
        return "No Cycle"


    # This is the second approach to the problem statement -Finf the length of the loop in the linked list 
    def Find_length(self):
        print("Second Method using the Floyds pointer method ---->",end="")
        if self.head is not None:
            slow=self.head
            fast=self.head.next
        else:
            return self.head 
        count=0
        while fast and fast.next is not None:
            if slow==fast:
                count+=1
                fast=fast.next
                while fast!=slow:
                    fast=fast.next
                    count+=1
                return count
            else:
                slow=slow.next
                fast=fast.next.next
        return "No loop detect "
                
# Display function to dispaly the linked list 
    def Dispaly(self):
        current=self.head
        while current:
            print(">>",current.data,end="")
            current=current.next
        print()

# Creation of the object and the calling of the methods from the Class 
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
links.Loop(45,l6)
# links.Dispaly()
print(links.Length_Of_Loop())
print(links.Find_length())
