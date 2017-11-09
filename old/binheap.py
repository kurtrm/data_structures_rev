"""Binary Min Heap."""


class BinHeap(object):
    """Min Heap Data Structure."""

    def __init__(self, iterable=[]):
        """Initialize an empty min heap."""
        if not isinstance(iterable, list):
            raise TypeError(
                'None or list types are the only valid arguments supported.')
        self._iterable = self.heapify(iterable)

    def heapify(self, iterable):
        """Function that will be used in init and other methods."""
        heap_list = iterable
        for item in heap_list[::-1]:
            item_index = heap_list.index(item)
            parent = (item_index - 1) // 2
            while item_index > 0:
                if heap_list[item_index] < heap_list[parent]:
                    curr_val = heap_list[parent]
                    heap_list[parent] = heap_list[item_index]
                    heap_list[item_index] = curr_val
                    item_index = parent
                    parent = (item_index - 1) // 2
                else:
                    break
        return heap_list

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
