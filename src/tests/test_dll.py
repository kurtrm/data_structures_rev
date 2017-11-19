"""Test double linked list class."""
import pytest


@pytest.fixture
def dll():
    """Instantiate a dll for testing."""
    from ..dll import DoubleLinkedList
    double_link = DoubleLinkedList()
    return double_link


def test_dll_initialization(dll):
    """Test that there's nothing initialized."""
    assert dll.tail is dll.head is None


def test_dll_push_pushes_value(dll):
    """Test that the push pushes a value to head of list."""
    dll.push(1)
    assert dll.tail.data == dll.head.data == 1


def test_dll_push_head_and_tail_change(dll):
    """Test if second item is pushed in. Head and tail are seperate values."""
    dll.push(1)
    dll.push(2)
    assert (dll.tail.data, dll.head.data) == (1, 2)


def test_dll_push_3(dll):
    """Test that if 3 vals are pushed there is a head, prior node and tail."""
    dll.push(1)
    dll.push(2)
    dll.push(3)
    assert (dll.tail.data, dll.head.next_node.next_node.data,
            dll.head != dll.head.next_node, dll.head.data, dll.head.next_node.prior_node.data,
            dll.tail.prior_node.data) == (1, 1, True, 3, 3, 2)


def test_dll_pop_index_error(dll):
    """Test that the Index Error is raised if no val is popped."""
    with pytest.raises(IndexError):
        dll.pop()


def test_snip_pop_index_error(dll):
    """Test of snip to get index error."""
    with pytest.raises(IndexError):
        dll.snip('tail')


def test_snip_shift_index_error(dll):
    """test that we get snip index error."""
    with pytest.raises(IndexError):
        dll.snip('head')


def test_snip_one_node(dll):
    """Test that head and tail are none and get correct val."""
    dll.append(3)
    popped = dll.snip('head')
    assert (3, dll.head, dll.tail) == (3, None, None)



def test_dll_pop_only_has_one_item_phase_one(dll):
    """Test that pop only has one item and both are head and tail none vals."""
    dll.push(1)
    dll.push(2)
    assert (dll.pop(), dll.head.data, dll.tail.data,
            dll.head.next_node) == (2, 1, 1, None)


def test_dll_pop_only_has_one_item_phase_two(dll):
    """Test that pop only has one item and both are head and tail none vals."""
    dll.push(1)
    dll.push(2)
    dll.pop()
    assert (dll.pop(), dll.head, dll.tail) == (1, None, None)


def test_dll_appends_a_value(dll):
    """Ensure tail and head are the same."""
    dll.append(1)
    assert dll.tail.data == dll.head.data == 1


def test_dll_appends_3_values(dll):
    """Verify node connections after appending 3 values."""
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert (dll.tail.data, dll.head.data, dll.head.prior_node,
            dll.tail.next_node, dll.tail.prior_node.data,
            dll.head.next_node.data, dll.head.next_node.prior_node.data,
            dll.tail.prior_node.next_node.data) == (3, 1, None,
                                                    None, 2, 2,
                                                    1, 3)


def test_dll_shift_only_has_one_item_phase_one(dll):
    """Test that node connections after shifting."""
    dll.push(1)
    dll.push(2)
    assert (dll.shift(), dll.head.data, dll.tail.data,
            dll.head.next_node, dll.tail.prior_node) == (1, 2, 2, None, None)


def test_dll_shift_only_has_one_item_phase_two(dll):
    """Test that node connections after shifting."""
    dll.push(1)
    dll.push(2)
    dll.shift()
    assert (dll.shift(), dll.head, dll.tail) == (2, None, None)


def test_dll_remove_phase_one(dll):
    """Testing the dll remove function."""
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.remove(3)
    assert (dll.head.next_node.data,
            dll.head.next_node.prior_node.data) == (2, 4)


def test_dll_remove_phase_two(dll):
    """Testing the dll remove function."""
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.remove(3)
    dll.remove(1)
    assert (dll.tail.data,
            dll.tail.prior_node.data) == (2, 4)


def test_dll_remove_phase_three(dll):
    """Testing the dll remove function."""
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.remove(3)
    dll.remove(1)
    dll.remove(4)
    assert dll.head.data == dll.tail.data == 2


def test_dll_size(dll):
    """Test to make sure we get the right number of nodes."""
    dll_lengths = []
    dll.push(1)
    dll.push(2)
    dll.append(3)
    dll.push(4)
    dll.push(5)
    dll.push(6)
    dll_lengths.append(dll.size())
    dll.remove(4)
    dll.pop()
    dll.shift()
    dll.pop()
    dll_lengths.append(dll.size())
    assert dll_lengths == [6, 2]


def test_dll_shift(dll):
    """Test index error when shifting from empty list."""
    with pytest.raises(IndexError):
        dll.shift()

def test_snip(dll):
    """Test the dry version of pop and shift."""

