
def MergeLists(headA, headB):
    if headA == None and headB == None:
        return None
        
    if headA == None:
        return headB
    
    if headB == None:
        return headA
        
    head = None
    if headA.data <= headB.data:
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next
        
    point = head
    while headA != None and headB != None:
        if headA.data <= headB.data:
            point.next = headA
            headA = headA.next
        else:
            point.next = headB
            headB = headB.next
        point = point.next
    if headA != None:
        point.next = headA
    if headB != None:
        point.next = headB
    
    return head