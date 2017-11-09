"""Test of the reversed linked list."""

import pytest


@pytest.fixture
def linked_list():
    """Make linked_list for testing."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3])
    return linked_list


def test_empty_linked_list(linked_list):
    """Test exception from empty linked_list."""
    from reverse_linked_list import reverse_linked_list
    linked_list.pop()
    linked_list.pop()
    linked_list.pop()
    with pytest.raises(IndexError):
        reverse_linked_list(linked_list)


def test_one_in_linked_list(linked_list):
    """Test get one time back with one item in list."""
    from reverse_linked_list import reverse_linked_list
    linked_list.pop()
    linked_list.pop()
    reverse_linked_list(linked_list)
    assert linked_list.head.data == 1


def test_two_in_linked_list(linked_list):
    """Test that it works with two items."""
    from reverse_linked_list import reverse_linked_list
    linked_list.pop()
    reverse_linked_list(linked_list)
    assert linked_list.head.data == 1


def test_reverse_linked_list(linked_list):
    """Test that we reverse the list."""
    from reverse_linked_list import reverse_linked_list
    reverse_linked_list(linked_list)
    assert linked_list.head.data == 1
    assert linked_list.head.next_node.data == 2
    assert linked_list.head.next_node.next_node.data == 3


def test_long_reverse_linked_list(linked_list):
    """Test that we reverse the list."""
    from reverse_linked_list import reverse_linked_list
    linked_list.push(4)
    linked_list.push(5)
    reverse_linked_list(linked_list)
    assert linked_list.head.data == 1
    assert linked_list.head.next_node.data == 2
    assert linked_list.head.next_node.next_node.data == 3
    assert linked_list.head.next_node.next_node.next_node.data == 4
    assert linked_list.head.next_node.next_node.next_node.next_node.data == 5
    assert linked_list.head.next_node.next_node.next_node.next_node.next_node is None
    reverse_linked_list(linked_list)
    assert linked_list.head.data == 5
    assert linked_list.head.next_node.data == 4
    assert linked_list.head.next_node.next_node.data == 3
    assert linked_list.head.next_node.next_node.next_node.data == 2
    assert linked_list.head.next_node.next_node.next_node.next_node.data == 1
    assert linked_list.head.next_node.next_node.next_node.next_node.next_node is None
