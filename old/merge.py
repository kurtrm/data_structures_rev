"""Implementation of merge sort in Python."""


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
    if not isinstance(lineup, (list, tuple, str)):
        raise TypeError("Input only a list/tuple of integers")

    if len(lineup) in [0, 1]:
        return lineup
    if len(lineup) == 2:
        if lineup[0] > lineup[1]:
            lineup[0], lineup[1] = lineup[1], lineup[0]
        return lineup

    mid = len(lineup) // 2
    left = merge_sort(lineup[:mid])
    right = merge_sort(lineup[mid:])

    ret_list = []
    while left or right:
        if left and right:
            if left[0] < right[0]:
                ret_list.append(left.pop(0))
            else:
                ret_list.append(right.pop(0))
        elif left and not right:
            ret_list.extend(left)
            break
        elif right and not left:
            ret_list.extend(right)
            break
    return ret_list
