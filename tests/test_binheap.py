"""Test min heap."""
import pytest
import random


@pytest.fixture
def empty_heap():
    """Instantiate a heap for testing."""
    from src.binheap import BinHeap
    min_heap = BinHeap()
    return min_heap


@pytest.fixture
def random_heap():
    """Generate a list for use in a heap."""
    from src.binheap import BinHeap
    iterable = list(
        set(
            [random.randint(0, 200) for _ in range(random.randrange(500))]
        )
    )
    min_heap = BinHeap(iterable)
    return min_heap


@pytest.fixture
def full_heap():
    """Instantiate a heap from a list for testing."""
    from src.binheap import BinHeap
    min_heap = BinHeap([67, 5, 32, 1, 0, 2, 4, 101, 94, 72])
    return min_heap


def test_heap_initialization_empty_heap(empty_heap):
    """Test that there's nothing initialized."""
    from src.binheap import BinHeap
    assert isinstance(empty_heap, BinHeap)


def test_heap_type_error():
    """Ensure TypeError if we pass anything but a list or None."""
    from src.binheap import BinHeap
    with pytest.raises(TypeError):
        test_heap = BinHeap(1, 2, 3, 4)


def test_heap_initialized_with_list(full_heap):
    """Test that there's stuff in there."""
    from src.binheap import BinHeap
    assert isinstance(full_heap, BinHeap)
    assert full_heap._iterable == [0, 1, 2, 67, 5, 32, 4, 101, 94, 72]


def test_heap_push_none(empty_heap):
    """Test that the heap won't let you push None."""
    with pytest.raises(TypeError):
        empty_heap.push()


def test_len(full_heap):
    """Verify length works on heap."""
    assert len(full_heap) == 10


def test_empty_heap_pop(empty_heap):
    """Test that the heap won't let you pop if it's empty."""
    with pytest.raises(IndexError):
        empty_heap.pop()


def test_successful_pop(full_heap):
    """Test that we get the smallest number when we pop."""
    # import pdb; pdb.set_trace()
    assert full_heap.pop() == 0
    assert full_heap._iterable[0] == 1
    assert full_heap.pop() == 1
    assert full_heap._iterable[0] == 2
    assert full_heap.pop() == 2
    assert full_heap._iterable[0] == 4
    assert len(full_heap) == 7


def test_successful_push(empty_heap):
    """Test that pushes are successful."""
    empty_heap.push(2)
    assert empty_heap._iterable[0] == 2
    empty_heap.push(55)
    assert empty_heap._iterable[0] == 2
    empty_heap.push(1)
    assert empty_heap._iterable[0] == 1
    assert empty_heap._iterable == [1, 55, 2]


def test_push_and_pop_dont_screw_with_each_other(full_heap):
    """Make sure they don't interfere with each other."""
    assert full_heap.pop() == 0
    assert full_heap._iterable[0] == 1
    full_heap.push(67)
    assert full_heap._iterable[0] == 1
    full_heap.push(0)
    assert full_heap._iterable[0] == 0


def test_big_random_heap(random_heap):
    """Make sure it works for a big ass heap."""
    for pop in random_heap._iterable:
        random_heap_min = min(random_heap._iterable)
        assert random_heap.pop() == random_heap_min


def test_push_non_integer(random_heap):
    """
    Ensure we raise an error when pushing a non-integer
    into the binheap.
    """
    with pytest.raises(TypeError):
        random_heap.push('heap')


def test_init_with_non_iterable():
    """
    Ensure we raise an error when trying to init with
    non integer.
    """
    from src.binheap import BinHeap
    with pytest.raises(ValueError):
        min_heap = BinHeap(777)
