"""Our queue for enqueue and dequeue."""
from .dll import DoubleLinkedList


class Queue(object):
    """Class Queue for enqueue and dequeue data structure."""

    def __init__(self):
        """Init for Queue."""
        self._dll = DoubleLinkedList()

    def enqueue(self, val):
        """Enqueue function for queue pushes value to head."""
        return self._dll.push(val)

    def dequeue(self):
        """Dequeue function for queue removes val from tail and returns val."""
        return self._dll.shift()

    def peek(self):
        """Return a new value without dequeuing it."""
        print(self._dll.tail.data)

    def size(self):
        """Length function for the queue."""
        return self._dll.size()

    def __len__(self):
        """Return the size method."""
        return self.size()
