def ReversePrint(head):
    if head == None:
        return
        
    if head.next != None:
        ReversePrint(head.next)
    
    print head.data