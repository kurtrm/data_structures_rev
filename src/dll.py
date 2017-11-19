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


class Node:
    """Node class for use in double linked list."""

    def __init__(self, data, next_node=None, prior_node=None):
        """Initialize a node when adding to the linked list."""
        self.data = data
        self.next_node = next_node
        self.prior_node = prior_node


class DoubleLinkedList:
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
            new_node = Node(val, self.head)
            self.head.prior_node = new_node
            self.head = new_node
        self._length += 1

    def append(self, val):
        """Append a val to the tail of a list."""
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(val)
        else:
            new_node = Node(val, None, self.tail)
            self.tail.next_node = new_node
            self.tail = new_node
        self._length += 1

    def insert(self, side, val):
        """
        Append a val to either the head or the tail. Accepts
        'tail' or 'head' as arguments to the side parameter.
        """
        if self.tail is None and self.head is None and side in ['head', 'tail']:
            self.tail = self.head = Node(val)
        else:
            if side == 'tail':
                new_node = Node(val, None, self.tail)
                self.tail.next_node = new_node
                self.tail = new_node
            elif side == 'head':
                new_node = Node(val, self.head)
                self.head.prior_node = new_node
                self.head = new_node
            else:
                raise ValueError("Side parameter accepts either 'end' or 'tail.'")
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
        self.head = self.head.next_node
        self.head.prior_node = None
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
        self.tail = self.tail.prior_node
        self.tail.next_node = None
        return shifted.data

    def snip(self, side):
        """
        Remove and return either the head or the tail.
        Like insert, accepts 'tail' or 'head'.
        """
        if not self.tail:
            raise IndexError(
                'There\'s nothing to remove from the linked list.')
        if self.head == self.tail and side in ['tail', 'head']:
            snipped = self.head
            self.tail = self.head = None
        else:
            if side == 'tail':
                snipped = self.tail
                self.tail = self.tail.prior_node
                self.tail.next_node = None
            elif side == 'head':
                snipped = self.head
                self.head = self.head.next_node
                self.head.prior_node = None
            else:
                raise ValueError("Side parameter accepts either 'end' or 'tail.'")
        self._length -= 1
        return snipped.data

    def size(self):
        """Return the length of the double linked list."""
        return self._length


# TODO: Refactor this
    def remove(self, val):
        """Remove a node with the value provided."""
        if self.head.data == val:
            self.pop()
        elif self.tail.data == val:
            self.shift()
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.data != val:
                    current_node = current_node.next_node
                else:
                    new_next_node = current_node.next_node
                    new_prior_node = current_node.prior_node
                    new_next_node.prior_node = new_prior_node
                    new_prior_node.next_node = new_next_node
                    self._length -= 1
                    break
