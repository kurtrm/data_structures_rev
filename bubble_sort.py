"""Classic bubble sort implementation."""
import random


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


def noisy_bubble_sort(lineup, noise_level=5):
    """
    Sort the iterable using the Bubble sort method.
    params
    -------
    lineup: list, tuple, or str

    return
    ------
    lineup: list, tuple, or str (in place)

    Same as the previous bubble_sort implementation except adjusts the given variable
    by a noise percentage at the time of comparison.
    """
    if not isinstance(lineup, (list, tuple, str)):
        raise TypeError("Input must be either list, tuple, or str")

    size = len(lineup)
    while size > 0:
        for idx, current in enumerate(lineup[:size]):
            if idx:
                prev = idx - 1
                prev_noisy = lineup[prev] + noise(noise_level)
                current_noisy = current + noise(noise_level)
                if prev_noisy > current_noisy:
                    lineup[prev], lineup[idx] = lineup[idx], lineup[prev]
        size -= 1
    return lineup


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
