class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def __init__(self):
        self.myhead=None

    def insert(self,data):
        if data==None:
            return None
        new_node=ListNode(data)
        if self.myhead==None:
            self.myhead=new_node
            return
        current=self.myhead
        while current and current.next is not None:
            current=current.next
        current.next=new_node

    def output(self):
        return self.myhead

    def insertionSortList(self, head):
        arr=[]
        current=head
        while current :
            arr.append(current.val)
            current=current.next

        for i in range(len(arr)):
            j=i
            while j>0 and arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j=j-1

        for i in arr:
            self.insert(i)

        return self.output()




