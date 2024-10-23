#Leetcode2095
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    lenght=0
    while cur:
        lenght+=1
        cur=cur.next
    midpoint = lenght//2
    if midpoint==0:
        head=head.next
        return head
    count = 0
    current=head
    while count!=midpoint-1:
        current = current.next
        count+=1
    current.next=current.next.next
    return head