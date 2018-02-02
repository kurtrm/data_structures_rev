"""Implementation of Bubble sort in Python."""


def bubble_sort(lineup):
    """
    Sort the iterable using the Bubble sort method.
    params
    -------
    lineup: list, tuple, or str

    return
    ------
    lineup: list, tuple, or str (in place)

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


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    random = Timer(
        'bubble_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import bubble_sort; from random import randint"
    )
    print("""
Bubble sort, sometimes referred to as sinking sort, is a simple
sorting algorithm that repeatedly steps through the list to be sorted,
compares each pair of adjacent items and swaps them if they are in the
wrong order.
""")
    print("Random input (100 numbers from 0-1000 sorted) over 1000 trials:")
    print(random.timeit(number=1000))
