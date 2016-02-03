
def RemoveDuplicates(head):
    if head == None:
        return None
    
    if head.next == None:
        return head
        
    first = head
    second = head.next
    
    while second != None:
        if first.data == second.data:
            first.next = second.next
        else:
            first = second
        second = first.next
    return head
        