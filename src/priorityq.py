"""Implement a priority queue using binary heap."""
from typing import List, Any, Union, Iterable
from collections import namedtuple


Node = namedtuple('Node', ['priority', 'value'])


class PriorityQueue:
    """Raw Python implementation of a priority queue."""

    def __init__(self, iterable: Union[None, Iterable[tuple]]=None) -> None:
        """
        Initialize our priority queue.
        Accepts a list of tuples.
        """
        self._length = 0
        try:
            self._heap = []
            for task in iterable:
                if task[0] == 0:
                    self.insert(task[1], float('inf'))
                else:
                    self.insert(task[0], task[1])
        except TypeError:
            if iterable is None:
                self._heap = []
            else:
                raise ValueError('Argument must be an iterable')

    def _sort_down(self, index: int=0) -> None:
        """
        """
        # import pdb; pdb.set_trace()
        left, right = (index * 2) + 1, (index * 2) + 2
        try:
            if self._heap[left].priority < self._heap[right].priority:
                idx, highest = left, self._heap[left]
            else:
                idx, highest = right, self._heap[right]
            if highest.priority < self._heap[index].priority:
                self._heap[idx], self._heap[index] = self._heap[index], self._heap[idx]
            self._sort_down(idx)
        except IndexError:
            pass

    def heapify(self) -> List:
        """Function to heapify our list of tuples (self._heap)."""
        idx = len(self._heap) - 1
        parent = (idx - 1) // 2
        while idx > 0:
            if self._heap[idx].priority > 0 and self._heap[idx].priority < self._heap[parent].priority:
                self._heap[parent], self._heap[idx] = self._heap[idx], self._heap[parent]
            idx = parent
            parent = (idx - 1) // 2

    def insert(self, value: Any, priority: Union[int, float]=float('inf')) -> None:
        """Insert a value into the priority queue with an optional priority."""
        if not isinstance(priority, int):
            if priority != float('inf'):
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
        try:
            self._heap[-1], self._heap[0] = self._heap[0], self._heap[-1]
            popped = self._heap.pop()
        except IndexError:
            raise IndexError("pop from empty priority queue")
        self._sort_down()

        return popped.value

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
