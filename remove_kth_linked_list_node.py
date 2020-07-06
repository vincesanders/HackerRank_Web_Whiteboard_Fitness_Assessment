def removeKthLinkedListNode(head, k): # Space: O(1) Time: O(n) n = length of linked list
    # Write your code here

    # Checking for an edge case. If a node wasn't passed in to the first parameter
    if head is None:
        return None

    # this is an artifact of my first pass solution - I forgot to delete it
    output = ''

    # this variable is used to keep track of the distance between the first pointer and the 2nd pointer.
    distance = 0
    p1 = head
    p2 = head
    num_of_nodes = 0

    # Traverse through linked list
    # We'll keep track of 2 pointers:
        # pointer 1's goal is to find the end of the list
        # pointer 2 will follow pointer 1 at k + 1 distance behind
            # the reason we're following  k + 1 distance, is because 
            # we need access to the node before the node that has to be removed, 
            # so it can easily be removed
    while p1 is not None:

        # Something I'd do different: I would only increment distance till I found the point
        # the second pointer would start traversing
        distance += 1

        # Once p1 gets ahead k + 1, we start moving p2 in step with it
        if distance > k + 1:
            p2 = p2.next
        p1 = p1.next
        num_of_nodes += 1

    # p2 will be the node before the node that has to be removed
    if num_of_nodes > k:
        # remove p2
        p2.next = p2.next.next

    # if the number of nodes is equal to k, then that means the head is what needs to be removed.
    if num_of_nodes is k:
        head = p2.next

    # return the head. At this point, all necessary changes have been made.
    return head