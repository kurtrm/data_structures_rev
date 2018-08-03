"""Binary Min Heap."""
from numbers import Number
from typing import Iterable, Union


class BinHeap:
    """Min Heap Data Structure."""

    def __init__(self, iterable: Union[None, Iterable]=None) -> None:
        """Initialize an empty min heap."""
        try:
            for num in iterable:
                self.push(num)
        except TypeError:
            if iterable is None:
                self._iterable = []
            else:
                raise ValueError('Argument must be an iterable')

    # def heapify(self, iterable: list) -> list:
    #     """Function that will be used in init and other methods."""
    #     for item in reversed(iterable):
    #         # import pdb; pdb.set_trace()
    #         idx = iterable.index(item)
    #         parent = (idx - 1) // 2
    #         while idx > 0 and iterable[idx] < iterable[parent]:
    #             iterable[parent], iterable[idx] = iterable[idx], iterable[parent]
    #             idx = parent
    #             parent = (idx - 1) // 2

    #     return iterable

    def heapify(self):
        """Function that will be used in init and other methods."""
        idx = len(self._iterable) - 1
        parent = (idx - 1) // 2
        while idx > 0 and self._iterable[idx] < self._iterable[parent]:
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
        popped = self._iterable.pop(0)
        self.heapify(self._iterable)

        return popped

    def __len__(self) -> int:
        """Return length of the binary heap."""
        return len(self._iterable)
