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
        if self.head==None:
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

# Main code starts here

    def splitListToParts(self, head, k):
        length=0
        arr=[]
        current=head
        while current:
            length+=1
            current=current.next

        remainder=length%k
        quotient=length//k

        if length<=k:
            x=k-length
            current=head
            while current:
                front=current.next
                current.next=None
                arr.append(current)
                current=front

            for i in range(x):
                arr.append([])

        else:
            temp_head=head
            count=0
            current_=head
            while current_:
                count+=1
                if count==remainder+quotient:
                    front=current_.next
                    current_.next=None
                    count=0
                    arr.append([temp_head])
                    current_=front
                    temp_head=front
                    remainder=0
                else:
                    current_=current_.next
        return arr

# main code ends here



arr=[0,1,2,3,4]
sol=Solution()
for i in arr:
    sol.insert(i)
header=sol.header()
sol.show(header)
print()
k=3
output=sol.splitListToParts(header,k)
print(output)
for i in range(len(output)):
    sol.show(output[i][0])
