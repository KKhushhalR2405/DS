class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LL:
    def __init__(self):
        self.head=None
        
    def insertbeg(self):
        self.value=input("Enter the value")
        new=node(self.value)
        if self.head==None:
            self.head=new
        else:
            new.next=self.head
            self.head=new
            
    def insertpos(self):
        self.value=input("Enter the value")
        self.pos=int(input("Enter position"))
        new=node(self.value)
        t=self.head
        for i in range(1,self.pos):
            if t!=None:
                t=t.next
            else:
                print("Position index greater than length")
                return
        
        new.next=t.next
        t.next=new
        
    def insertlast(self):
        self.value=input("Enter the value")
        new=node(self.value)
        if self.head==None:
            self.head=new
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=new
            
    def delbeg(self):
        if self.head==None:
            print("Nothing to delete")
        else:
            self.head=self.head.next
            print("Element deleted")
            
    def dellast(self):
        if self.head==None:
            print("Nothing to delete")
        else:
            t=self.head
            while t.next.next!=None:
                t=t.next
            t.next=None
            print("Element deleted")
            
    def delpos(self):
        if self.head==None:
            print("Nothing to delete")
        else:
            self.ind=int(input("Enter index to be deleted"))
            t=self.head
            for i in range(1,self.ind):
                t=t.next
            t.next=t.next.next
            print("Element deleted")
                
            
    def view(self):
        t=self.head
        while t!=None:
            print(t.data,end=" ")
            t=t.next
        print()


"""
                         Main function to test the LinkedList class

"""
        

print("1) Insert at beginning")
print("2) Insert at particular position")
print("3) Insert at last")
print("4) Delete at beginning")
print("5) Delete at particular position")
print("6) Delete at last")
print("7) View")

l=LL()

while True:
	a=int(input("Enter choice(Enter 0 to end) : "))
	if a==1:
		l.insertbeg()
	elif a==2:
		l.insertpos()
	elif a==3:
		l.insertlast()
	elif a==4:
		l.delbeg()
	elif a==5:
		l.delpos()
	elif a==6:
		l.dellast()
	elif a==0:
		print("Good bye !!!!!!!!!!")
		break
	elif a==7:
		l.view()

	else:
		print("Enter proper choice")
