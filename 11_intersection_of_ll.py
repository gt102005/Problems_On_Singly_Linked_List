# class Node to form the nodes of the linked list 
class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

# the class for creating the links between the nodes 
class Links(object):
    def __init__(self):
        self.head=None  
# Function Insert to add the node one after the another   
    def Insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current and current.next is not None:
            current=current.next
        current.next=new_node   
# function to dispaly the linked list 
    def Dispaly(self):
        current=self.head
        while current:
            print(">>",current.data,end="")
            current=current.next
        print()
    def Return_head(self):
        return self.head 

# class which will create a Y linked list having the intersection 
class Create_Intersection(object):
# function to perform the linking of the intersection point 
    def Create(self,headA,headB):
        currentA=headA
        currentB=headB
        while currentB and currentB.next is not None:
            currentB=currentB.next
        slow=headA
        fast=headA.next
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        currentB.next=slow
        return headA , headB
# Function to find the intersection point element 
    def Find_Intersection(self,first,second):
        list_=[]
        ftemp=first
        stemp=second
        while ftemp and ftemp.next is not None:
            list_.append(ftemp)
            ftemp=ftemp.next
        while stemp and stemp.next is not None:
            if stemp in list_:
                return stemp.data
            stemp=stemp.next
        return -1

# this is the first linked list 
arr1=[5,3,6,1,8,4,5]
link1=Links()
for i in arr1:
    link1.Insert(i)
head1=link1.Return_head()

# this is the second linked list 
arr2=[4,1,8,4,5,3]
link2=Links()
for i in arr2:
    link2.Insert(i)
head2=link2.Return_head()

# calling of the function for the creation od intersected linked list
create=Create_Intersection()
heads=create.Create(head1,head2)
output=create.Find_Intersection(heads[0],heads[1])
print(output)





