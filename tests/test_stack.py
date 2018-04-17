"""Our test file for our stack class."""
import pytest


@pytest.fixture
def the_stack():
    """Stack fixture."""
    from src.stack import Stack
    the_stack = Stack([1, 2, 3, 4])
    return the_stack


def test_instantiation(the_stack):
    """Test instantiation of the stack."""
    from src.stack import Stack
    assert (len(the_stack),
            isinstance(the_stack, Stack)) == (4, True)


def test_stack_push(the_stack):
    """Test for pushing to stack."""
    the_stack.push(5)
    assert the_stack._new_linked_list.head.data == 5


def test_stack_pop(the_stack):
    """Test for popping to stack."""
    assert (the_stack.pop(),
            the_stack._new_linked_list.head.data) == (4, 3)


def test_stack_pop_except_error():
    """Test for pop exception error and should get index errror."""
    from src.stack import Stack
    empty_stack = Stack()
    with pytest.raises(IndexError):
        empty_stack.pop()


def test_stack_len_of_stack(the_stack):
    """Test for length to stack."""
    assert len(the_stack) == 4


def test_search_stack():
    """Test to make sure stack is not accessing search method."""
    with pytest.raises(AttributeError):
        the_stack.search(4)


def test_remove_stack():
    """Test to make sure stack is not accessing remove method."""
    with pytest.raises(AttributeError):
        the_stack.remove(4)


def test_pop_and_push_combo_phase_one(the_stack):
    """Test to make sure we can push and pop together."""
    the_stack.push('stack')
    assert the_stack.pop() == 'stack'


def test_pop_and_push_combo_phase_two(the_stack):
    """Test to make sure we can push and pop together."""
    the_stack.push('stack')
    the_stack.push(34)
    assert (the_stack.pop(),
            the_stack.pop(),
            the_stack.pop()) == (34, 'stack', 4)


def test_pop_and_push_combo_phase_three(the_stack):
    """Test to make sure we can push and pop together."""
    the_stack.push('stack')
    the_stack.push(34)
    the_stack.push('wiener-dog')
    assert (the_stack.pop(),
            the_stack.pop(),
            the_stack.pop(),
            the_stack.pop()) == ('wiener-dog', 34, 'stack', 4)


def test_pop_and_push_combo_phase_four(the_stack):
    """Test to make sure we can push and pop together."""
    the_stack.push('stack')
    the_stack.push(34)
    the_stack.push('wiener-dog')
    the_stack.push(-123)
    assert (the_stack.pop(),
            the_stack.pop(),
            the_stack.pop(),
            the_stack.pop(),
            the_stack.pop()) == (-123, 'wiener-dog', 34, 'stack', 4)


def test_pop_and_push_combo_phase_five(the_stack):
    """Test to make sure we can push and pop together."""
    the_stack.push('stack')
    the_stack.push(34)
    the_stack.push('wiener-dog')
    the_stack.push(-123)
    assert (the_stack.pop(),
            the_stack.pop(),
            the_stack.pop(),
            the_stack.pop(),
            the_stack.pop(),
            the_stack.pop(),
            the_stack.pop(),
            the_stack.pop()) == (-123, 'wiener-dog', 34, 'stack', 4, 3, 2, 1)


def test_pop_and_push_combo_phase_six(the_stack):
    """Test to make sure we can push and pop together."""
    the_stack.push('stack')
    the_stack.push(34)
    the_stack.push('wiener-dog')
    the_stack.push(-123)
    the_stack.pop()
    the_stack.pop()
    the_stack.pop()
    the_stack.pop()
    the_stack.pop()
    the_stack.pop()
    the_stack.pop()
    the_stack.pop()
    with pytest.raises(IndexError):
        the_stack.pop()


def test_pop_and_push_combo_phase_seven(the_stack):
    """Test to make sure we can push and pop together."""
    the_stack.push('stack')
    the_stack.pop()
    the_stack.push(34)
    the_stack.pop()
    the_stack.pop()
    the_stack.pop()
    the_stack.push('wiener-dog')
    the_stack.pop()
    the_stack.pop()
    the_stack.push(-123)
    the_stack.pop()
    assert the_stack.pop() == 1
