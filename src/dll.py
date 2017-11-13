"""Write an implementation of linked lists in Python.

prior_node <- T
             (5)<-(3)<-('string')<-(bool)<-(dict)
             (5)->(3)->('string')->(bool)->(dict)
                                              H -> next_node
"""

"""
TODO: The head and tail are swapped...The tail's prev_node(prior_node)
should be pointing into the dll, not out. Same with head regarding next
node.
"""


class Node(object):
    """Node class for use in double linked list."""

    def __init__(self, data, next_node=None, prior_node=None):
        """Initialize a node when adding to the linked list."""
        self.data = data
        self.next_node = next_node
        self.prior_node = prior_node


class DoubleLinkedList(object):
    """Double linked version of a list."""

    def __init__(self):
        """Initialize an empty double linked list."""
        self._length = 0
        self.tail = None
        self.head = None

    def push(self, val):
        """Push a value to the head of the list."""
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(val)
        else:
            new_node = Node(val, None, self.head)
            self.head.next_node = new_node
            self.head = new_node
        self._length += 1

    def append(self, val):
        """Append a val to the tail of a list."""
        if self.tail is None and self.head is None:
            new_node = Node(val)
            self.tail = self.head = new_node
        else:
            new_node = Node(val, self.tail, None)
            self.tail.prior_node = new_node
            self.tail = new_node
        self._length += 1

    def pop(self):
        """Pop pops from the head of the list."""
        if not self.head:
            raise IndexError(
                'There\'s nothing to remove from the linked list.')
        self._length -= 1
        if self.head == self.tail:
            last_pop = self.head
            self.tail = self.head = None
            return last_pop.data
        popped = self.head
        self.head = self.head.prior_node
        self.head.next_node = None
        return popped.data

    def shift(self):
        """Remove the node from the tail of the list."""
        if not self.tail:
            raise IndexError(
                'There\'s nothing to remove from the linked list.')
        self._length -= 1
        if self.head == self.tail:
            last_pop = self.head
            self.tail = self.head = None
            return last_pop.data
        shifted = self.tail
        self.tail = self.tail.next_node
        self.tail.prior_node = None
        return shifted.data

    def size(self):
        """Return the length of the double linked list."""
        return self._length


# TODO: Refactor this
    def remove(self, val):
        """Remove a node with the value provided."""
        if self.head.data == val:
            self.pop()
            return
        elif self.tail.data == val:
            self.shift()
            return
        current_node = self.head
        while current_node is not None:
            if current_node.data != val:
                current_node = current_node.prior_node
            else:
                new_next_node = current_node.next_node
                new_prior_node = current_node.prior_node
                new_next_node.prior_node = new_prior_node
                new_prior_node.next_node = new_next_node
                self._length -= 1
                break
