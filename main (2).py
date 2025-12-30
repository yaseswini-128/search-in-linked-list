class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
def iterate(head):
    temp=head
    while temp!=None:
        print(temp.val,end=" ")
        temp=temp.next
        
def deleteNode(x,head):
    if head is None and head.next is None:
        return None
    if x==1:
        return head.next
    temp=head 
    cnt=0
    while cnt<x-1 and temp.next!=None:
        temp=temp.next
        cnt+=1 
    if temp.next!=None:
        temp.next=temp.next.next
    return head
    
    
head=Node(5)
head.next=Node(8)
head.next.next=Node(6)
head.next.next.next=Node(1)
head.next.next.next.next=Node(4)
head=deleteNode(2,head)
iterate(head)
