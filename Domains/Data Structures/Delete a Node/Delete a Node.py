def Delete(head, position):
    if position == 0:
        return head.next
    
    if position == 1:
        head.next = head.next.next
        return head
    
    point = head
    while position > 1:
        point = point.next
        position -= 1
    
    point.next = point.next.next
    return head