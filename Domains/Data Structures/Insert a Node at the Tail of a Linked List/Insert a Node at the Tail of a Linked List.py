def Insert(head, data):
    node = Node(data)
    if head == None:
        head = node
        return head
    
    point = head
    while point.next != None:
        point = point.next
    point.next = node
    return head