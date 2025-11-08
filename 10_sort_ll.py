class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
    def Merge(self):
        pass

class Linked_List(object):
    def __init__(self):
        self.head=None
    # Insert
    def Insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        current=self.head
        while current and current.next is not None:
            current=current.next
        current.next=new_node
    
    # it return head pointer
    def head_return(self):
        return self.head

    # Finds Mid
    def Mid(self,head):
        slow=head
        fast=head.next
        while fast and fast.next is not None:
            slow=slow.next 
            fast=fast.next.next
        return slow

    # Divides the linked list in halves
    def MergeSort(self,duplicate_head):
        if duplicate_head is None:
            return 
        if duplicate_head.next is None:
            return duplicate_head
        middle=self.Mid(duplicate_head)
        left=duplicate_head
        right=middle.next
        middle.next=None
        left=self.MergeSort(left)
        right=self.MergeSort(right)
        return self.SortLL(left,right)

    def SortLL(self,left,right):
        dummy_node=Node(-1)
        temp=dummy_node
        while left and right:
            if left.data >right.data:
                temp.next=right
                temp=right
                right=right.next
            else:
                temp.next=left
                temp=left
                left=left.next
        if left :
            temp.next=left
        if right:
            temp.next=right
        return dummy_node.next

    # Display
    def Display(self):
        current=self.head
        while current:
            print(">>",current.data,end="")
            current=current.next
        print()

    def Dispaly_Sorted(self,sorted_head):
        current=sorted_head
        while sorted_head:
            print(">>",sorted_head.data,end="")
            sorted_head=sorted_head.next
        print()



arr=test_case_20_plus = [2, 1, 0, 2, 1, 0, 1, 2, 0, 1, 1, 0, 2, 0, 1, 2, 1, 0, 2, 1, 0, 2, 2]

links=Linked_List()
for i in arr:
    links.Insert(i)
links.Display()
x=links.head_return()
sort=links.MergeSort(x)
print("Sorted Linked List : ")
links.Dispaly_Sorted(sort)


