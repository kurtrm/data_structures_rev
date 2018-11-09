"""Implementation of insertion sort in Python."""
from typing import Iterable


def insertion_sort(lineup: list) -> list:
    """Sort the iterable using the insertion sort method."""
    if not issubclass(type(lineup), Iterable):
        raise TypeError("argument must be iterable")
    # if not all(isinstance(x, (int, float)) for x in lineup):
    #     raise ValueError("Input only a list/tuple of integers")

    # Version 1.0
    #     move = lineup[idx]
    #     countdown = idx
    #     next_largest = idx
    #     while countdown > 0:
    #         if lineup[countdown - 1] > move:
    #             next_largest = countdown - 1
    #         countdown -= 1
    #     del lineup[idx]
    #     lineup.insert(next_largest, move)
    # return lineup

    # Version 1.1
    # lineup_copy = type(lineup)(lineup)
    # for idx in range(len(lineup)):
    #     candidate = lineup[idx]
    #     curr_idx = idx
    #     while curr_idx > 0:
    #         back_idx = curr_idx - 1
    #         prev_candidate = lineup_copy[back_idx]
    #         if candidate < prev_candidate:
    #             lineup_copy[curr_idx], lineup_copy[back_idx] = prev_candidate, candidate
    #         curr_idx -= 1
    # return lineup_copy

    # Version 1.2
    lineup_copy = type(lineup)(lineup)
    for idx in range(len(lineup_copy)):
        candidate = lineup_copy.pop(idx)
        curr_idx = idx
        while curr_idx > 0:
            back_idx = curr_idx - 1
            prev_candidate = lineup_copy[back_idx]
            if not candidate < prev_candidate:
                break
            else:
                curr_idx -= 1
        lineup_copy.insert(curr_idx, candidate)
    return lineup_copy


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    random = Timer(
        'insertion_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import insertion_sort; from random import randint"
    )
    print("""
Insertion sort iterates, consuming one input element each repetition,
and growing a sorted output list. At each iteration, insertion sort
removes one element from the input data, finds the location it belongs
within the sorted list, and inserts it there. It repeats until no input
elements remain.
""")
    print("Random input (100 numbers from 0-1000 sorted) over 1000 trials:")
    print(random.timeit(number=1000))
