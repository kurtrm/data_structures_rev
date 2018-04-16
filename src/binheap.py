"""Binary Min Heap."""


class BinHeap:
    """Min Heap Data Structure."""

    def __init__(self, iterable=None) -> None:
        """Initialize an empty min heap."""
        try:
            self._iterable = self.heapify(iterable)
        except TypeError:
            if iterable is None:
                self._iterable = []
            else:
                raise ValueError('Argument must be an iterable')

    def heapify(self, iterable):
        """Function that will be used in init and other methods."""
        for item in iterable[::-1]:
            idx = iterable.index(item)
            parent = (idx - 1) // 2
            while idx > 0 and iterable[idx] < iterable[parent]:
                iterable[parent], iterable[idx] = iterable[idx], iterable[parent]
                idx = parent
                parent = (idx - 1) // 2

        return iterable

    def push(self, val):
        """Push a value onto the heap."""
        if not isinstance(val, int):
            raise TypeError(
                'push() takes one argument, none provided')
        self._iterable.append(val)
        self._iterable = self.heapify(self._iterable)

    def pop(self):
        """Pop the min value from the heap, return it, and resort the heap."""
        if len(self._iterable) == 0:
            raise TypeError(
                'Cannot pop from empty heap.')
        popped = self._iterable.pop(0)
        self.heapify(self._iterable)
        return popped

    def __len__(self):
        """Return length of the binary heap."""
        return len(self._iterable)
