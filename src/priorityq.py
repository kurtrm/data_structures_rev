"""Implement a priority queue using binary heap."""
from typing import List, Any
from collections import namedtuple


Node = namedtuple('Node', ['priority', 'value'])


class PriorityQueue:
    """Raw Python implementation of a priority queue."""

    def __init__(self, iterable: Union[None, Iterable[tuple]]=None) -> None:
        """
        Initialize our priority queue.
        Accepts a list of tuples.
        """
        try:
            self._iterable = []
            for num in iterable:
                self.push(num)
        except TypeError:
            if iterable is None:
                self._iterable = []
            else:
                raise ValueError('Argument must be an iterable')


    def _sort_down(self, index=0): None:
        """
        """


    def heapify(self) -> List:
        """Function to heapify our list of tuples (self._heap)."""
        for item in self._heap[::-1]:
            current_node = self._heap.index(item)
            parent = (current_node - 1) // 2
            while current_node > 0:
                parent_priority = self._heap[parent].priority
                current_node_priority = self._heap[current_node].priority
                if current_node_priority > 0:
                    if parent_priority is 0 or parent_priority > current_node_priority:
                        curr_val = self._heap[parent]
                        self._heap[parent] = self._heap[current_node]
                        self._heap[current_node] = curr_val
                current_node = parent
                parent = (current_node - 1) // 2

    def insert(self, value: Any, priority: int=0) -> None:
        """Insert a value into the priority queue with an optional priority."""
        if not isinstance(priority, int):
            raise TypeError("Must provide an integer for priority.")
        if priority < 0:
            raise ValueError("You may not use a negative priority."
                             "Priority must be 0 or greater.")
        self._heap.append(Node(priority, value))
        if len(self._heap) > 1:
            self.heapify()
        self._length += 1

    def pop(self) -> List:
        """Pop function for removing highest priority item from queue."""
        pop_it = self._heap.pop(0)
        self.heapify()
        self._length -= 1
        return pop_it.value

    def peek(self) -> List:
        """Return the highest priority item without removing from queue."""
        return self._heap[0].value

    def size(self) -> int:
        """Return the size of our priority queue."""
        return self._length

    def __len__(self):
        """
        Return the size of the priority queue.
        """
        return self.size()
