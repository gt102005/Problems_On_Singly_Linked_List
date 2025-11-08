class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution(object):
    def __init__(self):
        self.head=None

    def insert(self,data):
        if data==None:
            return
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current and current.next is not None:
            current=current.next
        current.next=new_node

    def header(self):
        return self.head

    def show(self,head):
        current=head
        while current:
            print("->",current.data,end="")
            current=current.next
        print()


    def removeZeroSumSublists(self, head):
#         Yet to Write




nums=[1,2,-3,3,1]
sol=Solution()
for i in nums:
    sol.insert(i)
header=sol.header()
sol.show(header)
output=sol.removeZeroSumSublists(header)
sol.show(output)



