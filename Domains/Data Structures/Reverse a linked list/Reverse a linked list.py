

def Reverse(head):
    if head == None:
        return head
    if head.next == None:
        return head
        
    prepoint = head
    point = head.next
    prepoint.next = None
    while point != None:
        temp = point.next
        point.next = prepoint
        prepoint = point
        point = temp
    
    return prepoint