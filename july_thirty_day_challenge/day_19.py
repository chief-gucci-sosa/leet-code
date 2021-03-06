"""
Remove all elements from a linked list of integers that have value val.
"""
























































































































































































































def create_linked_list(arr: List[int]) -> ListNode:

    head = ListNode(arr[0])
    current = head
    for n in arr[1:]:
        current.next = ListNode(n)
        current = current.next
    return head


def create_array(head: ListNode) -> List[int]:

    output = []
    while head:
        output.append(head.val)
        head = head.next

    return output
