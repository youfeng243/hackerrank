
def CompareLists(headA, headB):
    if headA == None and headB == None:
        return 1
    if headA == None:
        return 0
    if headB == None:
        return 0
     
    while headA != None and headB != None:
        if headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next
    
    if headA == None and headB == None:
        return 1
    
    return 0