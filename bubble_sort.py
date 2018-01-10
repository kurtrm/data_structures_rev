"""Classic bubble sort implementation."""


def bubble_sort(lineup):
    """
    Sort the iterable using the Bubble sort method.
    params
    -------
    lineup: list, tuple, or str

    return
    ------
    lineup: list, tuple, or str

    Takes the size of the iterable and decrements this size
    after each iteration, as the last item in the iterable will be properly
    sorted. This implementation performs a lookback rather than a lookahead,
    thus we evaluate idx for a truthy integer when starting each iteration.
    """
    if not isinstance(lineup, (list, tuple, str)):
        raise TypeError("Input must be either list, tuple, or str")

    size = len(lineup)
    while size > 0:
        for idx, current in enumerate(lineup[:size]):
            if idx:
                prev = idx - 1
                if lineup[prev] > current:
                    lineup[prev], lineup[idx] = lineup[idx], lineup[prev]
        size -= 1
    return lineup
