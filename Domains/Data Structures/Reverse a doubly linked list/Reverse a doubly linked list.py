#Reverse a doubly linked list

def Reverse(head):
    if head == None:
        return None
        
    if head.next == None:
        return head
    
    first = head
    second = head.next
    
    while second != None:
        first.prev, first.next = first.next, first.prev
        first = second
        second = first.next
    first.prev, first.next = first.next, first.prev
    return first