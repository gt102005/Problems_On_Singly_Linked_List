class Node(object):
    def __init__(self,data):
        self.data=data
        self.vertical=None
        self.next=None

class Solution(object):
    def __init__(self):
        self.head=None
        self.temp_head=None



    def call_me(self):
        if self.head is None:
            self.head=self.temp_head
            self.temp_head=None
            return
        current=self.head
        while current and current.next:
            current=current.next
        current.next=self.temp_head
        self.temp_head=None
        return

    def insert_nodes(self,data):
        if data==None:
            self.call_me()
            return
        new_node=Node(data)
        if self.temp_head is None:
            self.temp_head=new_node
            return
        verti=self.temp_head
        while verti and verti.vertical is not None:
            verti=verti.vertical
        verti.vertical=new_node
        return
    def header(self):
        return self.head

    def print_list(self,head):
        current=head
        while current:
            print(current.data,"->",end="")
            temp=current.vertical
            while temp:
                print(temp.data,end=" ")
                temp=temp.vertical
            print("!",end="     ")
            current=current.next

sol=Solution()
dic={1:[2,3,4,5,None],2:[4,5,6,4,None],3:[2,3,4,None],4:[None]}
for i in dic:
    sol.insert_nodes(i)
    for j in range(len(dic[i])):
        sol.insert_nodes(dic[i][j])

head=sol.header()
sol.print_list(head)






