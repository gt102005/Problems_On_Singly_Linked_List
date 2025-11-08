class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
    
class BT(object):
    def __init__(self):
        self.root=None
    
    def insert(self,val):
        newnode=Node(val)
        if self.root==None:
            self.root=newnode
            return 
        current=self.root
        while current and current.next is not None:
            current=current.next
        current.next=newnode
        return newnode
    
    def getRoot(self):
        return self.root
    
    def traverse(self,x):
        current=x
        while current:
            print(" ",current.data,end=" ")
            current=current.next
            
    def reverse(self,x):
        current=x
        prev=None
        while current is not None:
            front=current.next
            current.next=prev
            prev=current
            current=front
        return prev
        
        
arr1=[5,6,2,6,3]
arr2=[6,7,8,0,5,7]
print(arr1)
print(arr2)
bt1=BT()
bt2=BT()
for i in arr1:
    bt1.insert(i)
for i in arr2:
    bt2.insert(i)

print()
print("-----------Root--------------")
a1_root=bt1.getRoot()
a2_root=bt2.getRoot()
print("root of arr1 : ",a1_root)
print("root of arr2 : ",a2_root)

print()
print("------------Reverse----------")
r1=bt1.reverse(a1_root)
r2=bt1.reverse(a2_root)
print("reverse of arr1 : ",r1)
print("reverse of arr2 :",r1)

print()
print("------------------Traverse----------------")
t1=bt1.traverse(r1)
print()
t2=bt2.traverse(r2)

print()
extra=0
 
while r1 or r2:
    sum=0
    if r1:
        sum+=r1.data
        r1=r1.next
    else:
        r1=None
        
    if r2:
        sum+=r2.data
        r2=r2.next
    else:
        r2=None
        
    if extra:
        sum+=extra
    extra=sum//10
    new_node=Node(sum%10)
    new_node.next=next_
    next_=new_node

temp=next_
output=bt1.traverse(temp)

    








    
        