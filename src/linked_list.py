"""Write an implementation of linked lists in Python."""


class Node:
    """Node for use in a linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node in linked list."""
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Linked version of a list."""

    def __init__(self, iterable=None):
        """Initialization rules for linked list."""
        self._length = 0
        self.head = None
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)
            self._length = len(iterable)
        elif iterable is not None:
            raise TypeError('Acceptable arguments: str, list, tuple, None')

    def push(self, val):
        """Push the new value to the head of the linked list."""
        new_node = Node(val, self.head)
        self._length += 1
        self.head = new_node

    def pop(self):
        """Remove the head of the linked list."""
        if not self.head:
            raise IndexError(
                'Cannot pop from empty linked list.')
        popped = self.head
        self.head = self.head.next_node
        popped.next_node = None
        self._length -= 1
        return popped.data

    def size(self):
        """Return the length of the linked list."""
        return self._length

    def __len__(self):
        """Interact with built-in len() function."""
        return self.size()

    # def search(self, val):
    #     """Search the nodes for the value provided."""
    #     current_node = self.head
    #     while current_node is not None:
    #         if current_node.data == val:
    #             return current_node.data
    #         current_node = current_node.next_node

    def search(self, val):
        """
        Alternate search method utilizing the iter special
        method.
        """
        for node in self:
            if node == val:
                return node

    def remove(self, val):
        """Remove node from anywhere in the linked list with the val."""
        if self.head.data != val:
            current_node = self.head
            while current_node.next_node is not None:
                if current_node.next_node.data == val:
                    current_node.next_node = current_node.next_node.next_node
                    break
                current_node = current_node.next_node
            else:
                raise ValueError('Value not found.')
        else:
            self.head = self.head.next_node
        self._length -= 1

    def display(self):
        """Present a visual representation of the linked list."""
        display_str = ''
        for i, node in enumerate(self, 1):
            if i == len(self):
                display_str += f'{node.data}'
            else:
                display_str += f'{node.data}, '
        return f'({display_str})'

    def __str__(self):
        """Interact with built-in print function."""
        return self.display()

    def __iter__(self):
        """Permit iteration over the linked list."""
        node = self.head
        for _ in range(self._length):
            yield node
            node = node.next_node
