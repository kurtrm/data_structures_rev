"""Reverse a linked list in place."""
from linked_list import LinkedList


def reverse_linked_list(linked_list, node=None, next_node=None):
    """
    Reverse a linked list in place without the use of another linked list.
    """
    if node is None and next_node is None:
        node = linked_list.head
        next_node = node.next_node
    if next_node.next_node is not None:
        current_node = reverse_linked_list(linked_list, next_node, next_node.next_node)
        current_node.next_node = node
        return node
    else:
        next_node.next_node = node
        linked_list.head = next_node
        return node


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4, 5])
    print(ll)
    print(ll.head.data)
    reverse_linked_list(ll)
    print(ll)
    print(ll.head.data)
