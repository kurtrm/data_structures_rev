"""
Module containing the insertion sort algorithm.
"""


def selection_sort(arr: list) -> list:
    """
    Complexity: O(n^2)
    Iterate over list, looking for min
    Find min
    Swap min with the last item in the list
    continue loop starting at i + 1
    """
    arr_copy = list(arr)
    for i in range(len(arr_copy)):
        iteration_min = None
        for j, num in enumerate(arr_copy[i:], i):
            if iteration_min is None or num < iteration_min:
                index = j
                iteration_min = num
        arr_copy[i], arr_copy[index] = arr_copy[index], arr_copy[i]

    return arr_copy
