def SortedInsert(head, data):
    node = Node(data)
    if head == None:
        head = node
        return head
    
    if data <= head.data:
        node.next = head
        head.prev = node
        head = node
        return head
    
    if head.next == None:
        head.next = node
        node.prev = head
        return head
    
    point = head
    while point.next != None:
        if data <= point.data:
            node.next = point
            node.prev = point.prev
            point.prev.next = node
            point.prev = node
            return head
        point = point.next
    
    if data >= point.data:
        point.next = node
        node.prev = point
    else:
        node.next = point
        node.prev = point.prev
        point.prev.next = node
        point.prev = node
        
    
    return head
    