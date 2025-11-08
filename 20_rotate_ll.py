"""
Example : list nodes : 1>>>2>>>3>>>4>>>5>>>6>>>7>>>8
                k    : 2
          output     : 7>>>8>>>1>>>2>>>3>>>4>>>5>>>6

"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=ListNode(data)
        if self.head==None:
            self.head=newnode
            return
        current=self.head
        while current and current.next is not None:
            current=current.next
        current.next=newnode
    def get_head(self):
        return self.head
    def show(self,head):
        current=head
        while current:
            print(">>",current.val,end=" ")
            current=current.next
        print()

    def rotateRight(self, head, k):
        
        
            

link=Solution()
arr=[1,3,4,56,657,67]
k=1
for i in arr:
    link.insert(i)

