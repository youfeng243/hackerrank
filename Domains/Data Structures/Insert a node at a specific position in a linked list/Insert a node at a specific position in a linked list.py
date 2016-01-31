def InsertNth(head, data, position):
    node = Node(data)
    if position == 0:
        node.next = head
        return node
    
    if position == 1:
        node.next = head.next
        head.next = node
        return head
    
    point = head
    while point.next != None and position > 1:
        point = point.next
        position -= 1
    
    node.next = point.next
    point.next = node
    
    return head