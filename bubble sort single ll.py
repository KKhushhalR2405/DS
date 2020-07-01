#Linked List sorting using Bubble sort

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class ll:
    def __init__(self):
        self.head=None
        
    def insert(self):
        new=node(int(input("Enter node data : ")))
        if not self.head:
            self.head=new
        else:
            new.next=self.head
            self.head=new
    
    def view(self):
        t=self.head
        while t!=None:
            print(t.data,end=" ")
            t=t.next
        print()
            
    def sortasc(self):
        i=self.head
        
        while i:
            j=i.next
            while j:
                if i.data>j.data:
                    i.data,j.data=j.data,i.data
                j=j.next
            i=i.next
            

l=ll()
l.insert()
l.insert()
l.insert()
l.insert()
l.insert()
l.view()
l.sortasc()
l.view()