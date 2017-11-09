"""Reverse a linked list in place."""


def reverse_linked_list(linked_list):
    """
    Reverse a linked list in place without the use of another linked list.
    """
    if len(linked_list) is 0:
        raise IndexError('There are no values to reverse.')
    elif len(linked_list) is 1:
        return linked_list
    previous_node = None
    current_node = linked_list.head
    next_node = current_node.next_node
    while current_node is not None:
        current_node.next_node = previous_node
        previous_node = current_node
        current_node = next_node
        if current_node is not None:
            next_node = current_node.next_node
            if current_node.next_node is None:
                linked_list.head = current_node
