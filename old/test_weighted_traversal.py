"""Test our depth first and breadth first traversal functions."""
import pytest


@pytest.fixture
def new_weighted_graph():
    """Graph for testing."""
    from weighted_graph import Weighted
    empty_graph = Weighted()
    return empty_graph


@pytest.fixture
def graph_no_edges():
    """Test graph with nodes only."""
    from weighted_graph import Weighted
    example_graph = Weighted()
    example_graph.add_node('BB')
    example_graph.add_node(82)
    example_graph.add_node(99)
    example_graph.add_node('AA')
    return example_graph


@pytest.fixture
def graph_with_edges():
    """Test graph with nodes only."""
    from weighted_graph import Weighted
    new_graph = Weighted()
    new_graph.add_node('A')
    new_graph.add_node('B')
    new_graph.add_node('C')
    new_graph.add_node('D')
    new_graph.add_node('E')
    new_graph.add_node('F')
    new_graph.add_edge('A', 'B', 2)
    new_graph.add_edge('A', 'C', 3)
    new_graph.add_edge('B', 'D', 7)
    new_graph.add_edge('B', 'E', 8)
    new_graph.add_edge('C', 'B', 10)
    new_graph.add_edge('F', 'A', 15)
    new_graph.add_edge('C', 'F', 4)
    return new_graph


def test_start_at_a(graph_with_edges):
    """Ensure we get a list of stuff starting at a."""
    from weighted_traversal import depth_first_traversal
    assert depth_first_traversal(graph_with_edges, 'A') == ['A', 'B', 'D', 'E', 'C', 'F']


def test_only_accepts_graph():
    """Ensure we can only pass in a graph."""
    from weighted_traversal import depth_first_traversal
    with pytest.raises(TypeError):
        depth_first_traversal([1, 2, 3])


def test_only_rejects_nonexistent_node():
    """Ensure we can't do this with a nonexistent node."""
    from weighted_traversal import depth_first_traversal
    with pytest.raises(TypeError):
        depth_first_traversal(graph_with_edges, 'Z')


def test_start_at_c(graph_with_edges):
    """Ensure we get a list of stuff starting at c."""
    from weighted_traversal import depth_first_traversal
    assert depth_first_traversal(graph_with_edges, 'C') == ['C', 'B', 'D', 'E', 'F', 'A']


def test_start_at_a_breadth(graph_with_edges):
    """Ensure we get a list of stuff at a with breadth."""
    from weighted_traversal import breadth_first_traversal
    assert breadth_first_traversal(graph_with_edges, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']


def test_start_at_c_breadth(graph_with_edges):
    """Ensure we get a list of stuff starting at c."""
    from weighted_traversal import breadth_first_traversal
    assert breadth_first_traversal(graph_with_edges, 'C') == ['C', 'B', 'F', 'D', 'E', 'A']


def test_breadth_only_accepts_graph():
    """Ensure we can only pass in a graph."""
    from weighted_traversal import breadth_first_traversal
    with pytest.raises(TypeError):
        breadth_first_traversal([1, 2, 3])


def test_breadth_only_rejects_nonexistent_node():
    """Ensure we can't do this with a nonexistent node."""
    from weighted_traversal import breadth_first_traversal
    with pytest.raises(TypeError):
        breadth_first_traversal(graph_with_edges, 'Z')
