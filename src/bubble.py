"""Classic bubble sort implementation."""

def bubble_sort(iterable):
    """Sort the iterable using the Bubble sort method."""
    if not isinstance(iterable, (list, tuple, str)):
        raise TypeError("Input only a list/tuple of integers")
    if not all(isinstance(x, (int, float)) for x in iterable):
        raise ValueError("Input only a list/tuple of integers")

    size = len(iterable)
    while size > 0:
        for idx, item in enumerate(iterable[:size]):
            # import pdb; pdb.set_trace()
            if idx:
                if iterable[idx - 1] > iterable[idx]:
                    tmp = iterable[idx - 1]
                    iterable[idx - 1] = iterable[idx]
                    iterable[idx] = tmp
        size -= 1
    return iterable