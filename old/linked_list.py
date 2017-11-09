"""Write an implementation of linked lists in Python."""


class Node(object):
    """Node for use in a linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node in linked list."""
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    """Linked version of a list."""

    def __init__(self, iterable=None):
        """Initialization rules for linked list."""
        self._length = 0
        self.head = None
        if type(iterable) in [str, list, tuple]:
            for item in iterable:
                self.push(item)
            self._length = len(iterable)
        elif iterable is not None:
            raise TypeError('Please give an iterable or don\'t type anything.')

    def push(self, val):
        """Push the new value to the head of the linked list."""
        if not val:
            raise ValueError('Please provide a not null value.')
        new_node = Node(val, self.head)
        self._length += 1
        self.head = new_node

    def pop(self):
        """Remove the head of the linked list."""
        if not self.head:
            raise IndexError(
                'There\'s nothing to remove from the linked list.')
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

    def search(self, val):
        """Search the nodes for the value provided."""
        current_node = self.head
        while current_node is not None:
            if current_node.data != val:
                current_node = current_node.next_node
            else:
                return current_node.data
        else:
            return

    def remove(self, val):
        """Removenode from anywhere in the linked list with the given value."""
        if val is None:
            raise IndexError(
                'That value is not in this particular linked list.')
        if self.head.data == val:
            self.pop()
            return
        current_node = self.head
        previous_node = self.head
        while current_node is not None:
            if current_node.data != val:
                previous_node = current_node
                current_node = current_node.next_node
                continue
            else:
                previous_node.next_node = current_node.next_node
                self._length -= 1
                break
        else:
            raise ValueError('Value not found.')

    def display(self):
        """Present a visual representation of the linked list."""
        node = self.head
        display_str = ' '
        while node is not None:
                display_str += ' '
                display_str += '\''
                display_str += str(node.data)
                display_str += '\''
                node = node.next_node
        display_str = ', '.join(display_str.split())
        return '{}{}{}'.format('(', display_str, ')')

    def __str__(self):
        """Interact with built-in print function."""
        return self.display()
