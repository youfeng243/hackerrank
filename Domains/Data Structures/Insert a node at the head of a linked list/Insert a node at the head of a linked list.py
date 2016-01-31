
def Insert(head, data):
    node = Node(data)
    if head == None:
        head = node
        return head
    
    node.next = head
    
    return node