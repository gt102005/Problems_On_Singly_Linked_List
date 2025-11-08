"""Boilerplate code for the linked list"""
class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
    
class Links(object):
    def __init__(self):
        self.root=None

    def push(self,val):
        newnode=Node(val)
        if self.root==None:
            self.root=newnode
            return
        current=self.root
        while current and current.next is not None:
            current=current.next
        current.next=newnode
        return
    
    def get_root(self):
        return self.root

    
    def show(self,root):
        current=root
        while current:
            print(current.val, end=" ")
            current=current.next
        print()
    

"""The main code starts here for the double of the node"""
def doubleIt(head):
    total=0
    current=head
    prev=None
    while current:
        total=(total*10)+current.val
        front=current.next
        current.next=prev
        prev=current
        current=front
    total=total*2
    current=prev
    prev=None
    while current:
        x=total%10
        current.val=x
        total-=x
        total=total//10
        front=current.next
        current.next=prev
        prev=current
        current=front
    if total!=0:
        newnode=Node(total)
        newnode.next=prev
        prev=newnode
    return prev
 
link=Links()
arr=[9,9,9]
for i in arr:
    link.push(i)
print("current linked list : ",end=" ")
x=link.get_root()
link.show(x)
temp=doubleIt(x)
print("after a double of list : ",end=" ")
link.show(temp)

    
