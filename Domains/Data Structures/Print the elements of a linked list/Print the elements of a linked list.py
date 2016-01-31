

def print_list(head):
    if head == None:
        return 
    while head != None:
        print head.data
        head = head.next