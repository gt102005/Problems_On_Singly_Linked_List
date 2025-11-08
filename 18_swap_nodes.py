class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
    
class Links(object):
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return 
        current=self.head
        while current and current.next is not None:
            current=current.next
        current.next=newnode

    def get_root(self):
        return self.head
    
    def traverse(self,root):
        current=root
        while current:
            print(">>",current.val,end=" ")
            current=current.next
        print()

class Solution(object):
    def swapNodes(self,head,k):
        count=0
        current=head
        while current:
            count+=1
            current=current.next
        first=head
        for _ in range(k-1):
            first=first.next
        second=head
        for _ in range(count-k):
            second=second.next
        first.val,second.val=second.val,first.val
        return head
        





arr=[7,9,6,6,7,8,3,0,9,5]
k=5
link=Links()
for i in arr:
    link.insert(i)
head=link.get_root()
link.traverse(head)
solution=Solution()
sol=solution.swapNodes(head,k)
link.traverse(sol)




        




    
