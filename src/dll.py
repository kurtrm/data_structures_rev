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
from typing import Any


class Node:
    """Node class for use in double linked list."""

    def __init__(self, data: Any, next_node: 'Node'=None, prior_node: 'Node'=None) -> None:
        """Initialize a node when adding to the linked list."""
        self.data = data
        self.next_node = next_node
        self.prior_node = prior_node


class DoubleLinkedList:
    """Double linked version of a list."""

    def __init__(self) -> None:
        """Initialize an empty double linked list."""
        self._length = 0
        self.tail = None
        self.head = None

    def push(self, val: Any) -> None:
        """Push a value to the head of the list."""
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(val)
        else:
            new_node = Node(val, self.head)
            self.head.prior_node = new_node
            self.head = new_node
        self._length += 1

    def append(self, val: Any) -> None:
        """Append a val to the tail of a list."""
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(val)
        else:
            new_node = Node(val, None, self.tail)
            self.tail.next_node = new_node
            self.tail = new_node
        self._length += 1

    def insert(self, side: str, val: Any) -> None:
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
                raise ValueError("Side parameter accepts either 'head' or 'tail.'")
            self._length += 1

    def pop(self) -> Any:
        """Pop pops from the head of the list."""
        if not self.head:
            raise IndexError(
                "Cannot pop from empty double linked list.")
        self._length -= 1
        if self.head == self.tail:
            last_pop = self.head
            self.tail = self.head = None
            return last_pop.data
        popped = self.head
        self.head = self.head.next_node
        self.head.prior_node = None
        return popped.data

    def shift(self) -> Any:
        """Remove the node from the tail of the list."""
        if not self.tail:
            raise IndexError(
                "Cannot pop from empty double linked list.")
        self._length -= 1
        if self.head == self.tail:
            last_pop = self.head
            self.tail = self.head = None
            return last_pop.data
        shifted = self.tail
        self.tail = self.tail.prior_node
        self.tail.next_node = None
        return shifted.data

    def snip(self, side: str) -> None:
        """
        Remove and return either the head or the tail.
        Like insert, accepts 'tail' or 'head'.
        """
        if not self.tail:
            raise IndexError(
                "Cannot pop from empty double linked list.")
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
                raise ValueError("Side parameter accepts either 'head' or 'tail.'")
        self._length -= 1
        return snipped.data

    def size(self) -> int:
        """Return the length of the double linked list."""
        return self._length

    def remove(self, val: Any) -> None:
        """Remove a node with the value provided."""
        if self.head.data == val:
            self.pop()
        elif self.tail.data == val:
            self.shift()
        else:
            for node in self:
                if node.data == val:
                    new_next_node = node.next_node
                    new_prior_node = node.prior_node
                    new_next_node.prior_node = new_prior_node
                    new_prior_node.next_node = new_next_node
                    self._length -= 1
                    break

    def search(self, val: Any, start: str='head') -> 'Node':
        """
        Search the doubly linked list for a value. start parameter denotes
        on which end the search should start from.
        """
        for node in self:
            if node.data == val:
                return node

    def __contains__(self, val: Any) -> None:
        """Allows the use of the 'in' operator."""
        try:
            return val == self.search(val).data
        except AttributeError:
            return False

    def __iter__(self) -> 'Node':
        """Allow iteration over the doubly linked list."""
        node = self.head
        for _ in range(self._length):
            yield node
            node = node.next_node

    def __getitem__(self, val) -> 'Node':
        """
        Implemented in order to use the __reversed__ special method.
        """
        return self.search(val)

    def __setitem__(self, val, other) -> 'Node':
        """
        Implemented for safety.
        """
        pass

    def __len__(self) -> int:
        """
        Returns the size of the doubly linked list.
        """
        return self._length

    def __reversed__(self) -> 'Node':
        """
        Allow the doubly linked list to be iterated over in reverse.
        """
        node = self.tail
        for _ in range(self._length):
            yield node
            node = node.prior_node
