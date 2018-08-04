"""Binary Min Heap."""
from numbers import Number
from typing import Iterable, Union


class BinHeap:
    """Min Heap Data Structure."""

    def __init__(self, iterable: Union[None, Iterable]=None) -> None:
        """Initialize an empty min heap."""
        try:
            self._iterable = []
            for num in iterable:
                self.push(num)
        except TypeError:
            if iterable is None:
                self._iterable = []
            else:
                raise ValueError('Argument must be an iterable')

    def sort_down(self, index=0):
        """
        Starting from the top position, sort down the items in the list to get the max at the top.
        """
        try:
            if index:
                left, right = (index * 2) + 1, (index * 2) + 2
            else:
                left, right = 1, 2
            if self._iterable[left] < self._iterable[right]:
                idx, highest = left, self._iterable[left]
            else:
                idx, highest = right, self._iterable[right]
            if highest < self._iterable[index]:
                self._iterable[idx], self._iterable[index] = self._iterable[index], self._iterable[idx]
            self.sort_down(idx)
        except IndexError:
            pass

    def heapify(self):
        """Function that will be used in init and other methods."""
        idx = len(self._iterable) - 1
        parent = (idx - 1) // 2
        while idx > 0:
            if self._iterable[idx] < self._iterable[parent]:
                self._iterable[parent], self._iterable[idx] = self._iterable[idx], self._iterable[parent]
            idx = parent
            parent = (idx - 1) // 2

    def push(self, val: Union[int, float]) -> None:
        """Push a value onto the heap."""
        if not isinstance(val, Number):
            raise TypeError('Argument must be an integer or float')
        self._iterable.append(val)
        self.heapify()

    def pop(self) -> None:
        """Pop the min value from the heap, return it, and resort the heap."""
        try:
            self._iterable[-1], self._iterable[0] = self._iterable[0], self._iterable[-1]
            popped = self._iterable.pop()
        except IndexError:
            raise IndexError("pop from empty heap")

        self.sort_down()

        return popped

    def __len__(self) -> int:
        """Return length of the binary heap."""
        return len(self._iterable)
