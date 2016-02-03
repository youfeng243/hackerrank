

def HasCycle(head):
    if head == None:
        return 0
    if head.next == None:
        return 0
    fast = head.next
    slow = head
    
    while fast != None and slow != None:
        if fast == slow:
            return 1
        slow = slow.next
        fast = fast.next
        if fast != None:
            fast = fast.next
    
    return 0
    