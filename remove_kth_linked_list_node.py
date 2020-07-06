def removeKthLinkedListNode(head, k):
    # Write your code here
    if head is None:
        return None
    output = ''
    distance = 0
    p1 = head
    p2 = head
    num_of_nodes = 0
    while p1 is not None:
        distance += 1
        if distance > k + 1:
            p2 = p2.next
        p1 = p1.next
        num_of_nodes += 1
    # p2 will be the node before the node that has to be removed
    if num_of_nodes > k:
        # remove p2
        p2.next = p2.next.next
    if num_of_nodes is k:
        head = p2.next
    return head