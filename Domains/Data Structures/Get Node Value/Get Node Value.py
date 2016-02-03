
def GetNode(head, position):
    
    length = 0
    point = head
    
    while point != None:
        length += 1
        point = point.next
    
    index = length - position - 1
    
    if head == None:
        return 0
    
    if index == 0:
        return head.data
    
    while index > 0:
        head = head.next
        index -= 1
    
    return head.data
        
    