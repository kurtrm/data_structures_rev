"""Test bubble sort."""


import pytest
from random import randint


to_sort = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 17, 6, 300, 4, 3, 2, 11], [2, 3, 4, 6, 8, 9, 10, 11, 17, 300])
]


def test_bubble_non_list_raises_error():
    """Entering a non-list/tuple param raises an error."""
    from src.bubble import bubble_sort
    with pytest.raises(TypeError):
        bubble_sort({1: 'three', 2: 'seven'})


def test_bubble_non_int_raises_error():
    """Entering an iterable containing non-integers raises an error."""
    from src.bubble import bubble_sort
    with pytest.raises(TypeError):
        bubble_sort([1, 2, 3, 5, 'burp'])


@pytest.mark.parametrize('input_list, expected', to_sort)
def test_bubble_sort_returns_ordered_list(input_list, expected):
    """Bubble sort returns an ordered list."""
    from src.bubble import bubble_sort
    assert bubble_sort(input_list) == expected


def test_bubble_sort_sorts_random_list():
    """Bubble sort returns an ordered list."""
    from src.bubble import bubble_sort
    input_list = [randint(0, 1000) for i in range(100)]
    expected = sorted(input_list)
    assert bubble_sort(input_list) == expected
