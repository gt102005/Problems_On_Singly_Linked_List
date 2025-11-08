class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class Links(object):
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

# This is the first way of the checking the linked list whether palindrome or not 
    def CheckPalindrome(self):
        current=self.head
        list_=[]
        while current:
            list_.append(current.data)
            current=current.next
        current=self.head
        while current and current.next is not None:
            if list_[-1]==current.data:
                current=current.next
                list_.pop()
            else:
                print(current.data)
                return False
        return True
        
# this is the second approach of the checkin linked list palindrome
    def Check(self):
        pass

    def Dispaly(self):
        current=self.head
        while current:
            print("-->>",current.data,end="")
            current=current.next
        print()

arr=[1,2,3,2,1]
links=Links()
for i in arr:
    links.Insert(i)
links.Dispaly()
print(links.CheckPalindrome())