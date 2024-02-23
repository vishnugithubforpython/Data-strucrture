class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        return
class linkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        if self.head is None:
            print("the linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=linkedlist()
n1=node(10)
l.head=n1
n2=node(20)
l.head.next=n2
n3=node(30)
n2.next=n3
l.display()






