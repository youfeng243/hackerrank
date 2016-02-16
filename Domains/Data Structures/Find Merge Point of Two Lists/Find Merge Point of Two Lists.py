
def FindMergeNode(headA, headB):
    lengthA = 0
    lengthB = 0
    
    pointA = headA
    while pointA != None:
        lengthA += 1
        pointA = pointA.next
    
    pointB = headB
    while pointB != None:
        lengthB += 1
        pointB = pointB.next
    
    pointA = headA
    pointB = headB
    
    while lengthA > lengthB:
        pointA = pointA.next
        lengthA -= 1
    
    while lengthB > lengthA:
        pointB = pointB.next
        lengthB -= 1
    
    if pointA == pointB:
        return pointA.data
    
    while pointA.next != pointB.next:
        pointA = pointA.next
        pointB = pointB.next
    
    return pointA.next.data