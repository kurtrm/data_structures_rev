"""Our queue for enqueue and dequeue."""


from dll import DoubleLinkedList


class Queue(object):
    """Class Queue for enqueue and dequeue data structure."""

    def __init__(self):
        """Init for Queue."""
        self._new_dll = DoubleLinkedList()

    def enqueue(self, val):
        """Enqueue function for queue pushes value to head."""
        return self._new_dll.push(val)

    def dequeue(self):
        """Dequeue function for queue removes val from tail and returns val."""
        return self._new_dll.shift()

    def peek(self):
        """Return a new value without dequeuing it."""
        print(self._new_dll.tail.data)

    def size(self):
        """Length function for the queue."""
        return self._new_dll.size()

    def __len__(self):
        """Length."""
        return self._new_dll.size()
