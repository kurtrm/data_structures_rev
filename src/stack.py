"""Our stack for linked list."""


from .linked_list import LinkedList


class Stack:
    """Class stack."""

    def __init__(self, data=None):
        """Init for stack."""
        self._new_linked_list = LinkedList(data)

    def push(self, val):
        """Add a value to the top of the stack."""
        self._new_linked_list.push(val)

    def pop(self):
        """Remove and return the top of the stack."""
        if len(self) == 0:
            raise IndexError(
                'Cannot pop from empty stack.')
        return self._new_linked_list.pop()

    def __len__(self):
        """Return the number of items in the stack."""
        return self._new_linked_list.size()
