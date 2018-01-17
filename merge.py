"""Implementation of merge sort in Python."""
import random


def merge_sort(lineup):
    """
    Sort the lineup using the merge sort method.
    params
    -----
    lineup: list, tuple, or str

    returns
    -----
    lineup: list, tuple, or str

    Takes the midpoint of the iterable then recursively calls merge_sort on
    the iterable until it becomes falsey.
    """
    if not isinstance(lineup, (list, tuple)):
        raise TypeError("Input only a list/tuple of integers")

    if len(lineup) in [0, 1]:
        return lineup
    mid = len(lineup) // 2
    left = merge_sort(lineup[:mid])
    right = merge_sort(lineup[mid:])

    ranked = []
    while left or right:
        if left and right:
            if left[0] < right[0]:
                ranked.append(left.pop(0))
            else:
                ranked.append(right.pop(0))
        elif left and not right:
            ranked.extend(left)
            break
        elif right and not left:
            ranked.extend(right)
            break
    return ranked


def noisy_merge_sort(lineup, noise_level=5):
    """
    Sort the lineup using the merge sort method.
    params
    -----
    lineup: list, tuple, str, ndarray

    return
    -----
    ranked: list, tuple, or str

    Takes the midpoint of the iterable then recursively calls merge_sort on
    the iterable until it becomes falsey.
    """
    if not isinstance(lineup, (list, tuple)):
        raise TypeError("Input only a list/tuple of integers")
    if len(lineup) in [0, 1]:
        return lineup
    mid = len(lineup) // 2
    left = noisy_merge_sort(lineup[:mid])
    right = noisy_merge_sort(lineup[mid:])

    ranked = []
    while left or right:
        if left and right:
            noisy_left = left[0] + noise(noise_level)
            noisy_right = right[0] + noise(noise_level)
            if noisy_left < noisy_right:
                    ranked.append(left.pop(0))
            else:
                    ranked.append(right.pop(0))
        elif left and not right:
            ranked.extend(left)
            break
        elif right and not left:
            ranked.extend(right)
            break
    return ranked


def noise(level=5):
    """
    Parameters
    ----------
    {integer} : Threshold for the randomized variability

    Returns
    -------
    {integer} : Randomly generated interval [-5, 5]
    """
    if level >= 0 and level <= 100:
        return random.randint(-level, level + 1)
    else:
        raise ValueError('Enter a value between 0 and 100')
