"""Test for Deque Composition."""
import pytest


@pytest.fixture
def the_deque():
    """Queue fixture."""
    from ..deque import Deque
    the_deque = Deque()
    return the_deque


def test_the_deque_append(the_deque):
    """Test for enqueuing to the queue."""
    the_deque.append(2)
    assert the_deque._new_dll.head.data == 2
    assert the_deque._new_dll.tail.data == 2


def test_the_deque_append_multi_values(the_deque):
    """Test for enqueuing multiple values to the queue."""
    the_deque.append(2)
    the_deque.append(3)
    the_deque.append(4)
    the_deque.append(5)
    assert the_deque._new_dll.head.data == 5
    assert the_deque._new_dll.tail.data == 2
    assert the_deque._new_dll.head.next_node.data == 4
    assert the_deque._new_dll.tail.prior_node.data == 3


def test_the_deque_popleft(the_deque):
    """Test for dequeuing to the queue."""
    the_deque.append(2)
    assert the_deque.popleft() == 2


def test_the_deque_popleft_raises_exception(the_deque):
    """Test that if queue is empty the error is raised."""
    with pytest.raises(IndexError):
        the_deque.popleft()


def test_the_deque_popleft_multi_values_phase_1(the_deque):
    """Test for popleft on mulitple values."""
    the_deque.append(2)
    assert the_deque._new_dll.tail.data == 2


def test_the_deque_popleft_multi_values_phase_2(the_deque):
    """Test for popleft on mulitple values."""
    the_deque.append(2)
    the_deque.append(3)
    assert the_deque._new_dll.tail.prior_node.data == 3


def test_the_deque_popleft_multi_values_phase_3(the_deque):
    """Test for popleft on mulitple values."""
    the_deque.append(2)
    the_deque.append(3)
    the_deque.append(4)
    the_deque.append(5)
    assert the_deque._new_dll.head.data == 5


def test_the_deque_popleft_multi_values_phase_4(the_deque):
    """Test for popleft on mulitple values."""
    the_deque.append(2)
    the_deque.append(3)
    the_deque.append(4)
    the_deque.append(5)
    the_deque.popleft()
    assert the_deque._new_dll.tail.data == 3
    assert (the_deque.popleft(),
            the_deque._new_dll.tail.data) == (3, 4)


def test_the_pop(the_deque):
    """Test the peek function."""
    the_deque.append(1)
    the_deque.append(2)
    the_deque.append(3)
    assert the_deque._new_dll.head.data == 3
    the_deque.pop()
    assert the_deque._new_dll.head.data == 2


def test_the_appendleft(the_deque):
    """Test the peek left function."""
    the_deque.appendleft(1)
    the_deque.appendleft(2)
    the_deque.appendleft(3)
    assert the_deque._new_dll.tail.data == 3
    the_deque.popleft()
    assert the_deque._new_dll.tail.data == 2


def test_the_deque_size(the_deque):
    """Test the length on the queue."""
    the_deque.append(1)
    the_deque.append(2)
    the_deque.append(3)
    assert the_deque.size() == 3


def test_deque_peek(the_deque):
    """Test that we get the right value for peek."""
    the_deque.append(1)
    the_deque.append(2)
    the_deque.append(3)
    the_deque.appendleft('tables')
    assert the_deque.peek() == 3


def test_deque_peekleft(the_deque):
    """Test that we get the right value for peek."""
    the_deque.append(1)
    the_deque.append(2)
    the_deque.append(3)
    the_deque.appendleft('tables')
    assert the_deque.peekleft() == 'tables'


def test_deque_len(the_deque):
    """Test that we get the appropriate deque length interaction."""
    the_deque.append(1)
    the_deque.append(2)
    the_deque.append(3)
    the_deque.appendleft('tables')
    assert len(the_deque) == 4
