"""Test our graph implementation."""
import pytest
from basic_graph import Graph


@pytest.fixture
def new_graph():
    """Graph for testing."""
    from basic_graph import Graph
    empty_graph = Graph()
    return empty_graph


@pytest.fixture
def graph_no_edges():
    """Test graph with nodes only."""
    from basic_graph import Graph
    example_graph = Graph()
    example_graph.add_node('Grapefruit')
    example_graph.add_node(82)
    example_graph.add_node(99)
    example_graph.add_node('Luftballons')
    return example_graph


@pytest.fixture
def graph_with_edges():
    """Test graph with nodes only."""
    from basic_graph import Graph
    example_graph = Graph()
    example_graph.add_node('Grapefruit')
    example_graph.add_node(82)
    example_graph.add_node(99)
    example_graph.add_node('Luftballons')
    example_graph.add_edge(99, 'Luftballons')
    example_graph.add_edge('Grapefruit', 'Luftballons')
    example_graph.add_edge('Grapefruit', 82)
    return example_graph


def test_graph_init_success(new_graph):
    """Ensure our new graph is in fact a graph."""
    assert isinstance(new_graph, Graph)


def test_graph_adds_and_lists_nodes(graph_no_edges):
    """Ensure we get list of nodes."""
    listy = ['Grapefruit', 82, 99, 'Luftballons']
    for node in listy:
        assert node in graph_no_edges.nodes()


def test_contains(graph_no_edges):
    """Ensure we can use the 'in' operator."""
    node_list = ['Grapefruit', 82, 99, 'Luftballons', 3]
    assert all(node in graph_no_edges for node in node_list)


def test_graph_adds_nodes_and_edges(graph_no_edges):
    """Ensure we add edges to the nodes."""
    graph_no_edges.add_edge('Louisiana Crawfish', 'WA Invasive Species')
    assert graph_no_edges.edges() == [(
        'Louisiana Crawfish', 'WA Invasive Species')]


def test_graph_lists_adds_and_lists_edges(graph_no_edges):
    """Ensure we add edges to the nodes."""
    graph_no_edges.add_edge(82, 34)
    graph_no_edges.add_edge(99, 'Luftballons')
    assert (82, 34) in graph_no_edges.edges()
    assert (99, 'Luftballons') in graph_no_edges.edges()


def test_graph_deletes_nodes(graph_with_edges):
    """Ensure we can delete a node."""
    graph_with_edges.del_nodes('Grapefruit')
    listy = [82, 99, 'Luftballons']
    for node in listy:
        assert node in graph_with_edges.nodes()


def test_graph_cant_delete_an_unpresent_node(graph_no_edges):
    """Ensure we can't delete that doesn't exist."""
    with pytest.raises(ValueError):
        graph_no_edges.del_nodes(3.14)


def test_graph_cant_delete_without_argument(graph_no_edges):
    """Ensure we can't delete without an argument."""
    with pytest.raises(TypeError):
        graph_no_edges.del_nodes()


def test_del_some_edges(graph_with_edges):
    """Ensure we delete edges."""
    graph_with_edges.del_edges('Grapefruit', 'Luftballons')
    assert graph_with_edges._graph['Grapefruit'] == [82]


def test_cant_delete_nonexistent_edge(graph_with_edges):
    """Ensure we can't delete a nonexistent edge."""
    with pytest.raises(ValueError):
        graph_with_edges.del_edges('Grapefruit', 'Badgers')


def test_nodes_exist(graph_no_edges):
    """Ensure we can assert nodes are in a graph."""
    for node in graph_no_edges._graph:
        assert graph_no_edges.has_node(node)


def test_false_if_no_node(graph_no_edges):
    """Ensure we get false."""
    false_nodes = ['land submarine', 'Portland Timbers', 'tug cable scope', 100]
    for node in false_nodes:
        assert graph_no_edges.has_node(node) is False


def test_node_neighbors(graph_no_edges):
    """Ensure we get the right neighbors for a node."""
    graph_no_edges.add_edge('Grapefruit', 82)
    assert graph_no_edges.neighbors('Grapefruit') == [82]


def test_node_without_neighbors(graph_no_edges):
    """Ensure we get None back for neighbors."""
    assert graph_no_edges.neighbors(99) == []


def test_node_error_if_nonpresent(graph_no_edges):
    """Can not get neighbors of nonpresent node."""
    with pytest.raises(ValueError):
        graph_no_edges.adjacent('Raccoon', 'Rocket')


def test_adjacent_nodes(graph_with_edges):
    """Ensure we get adjacent edges."""
    assert graph_with_edges.adjacent(99, 'Luftballons')


def test_adjacent_none(graph_with_edges):
    """Ensure we get false."""
    assert graph_with_edges.adjacent(82, 'Grapefruit') is False


def test_adjacent_unpresent(graph_with_edges):
    """Ensure we get an error."""
    with pytest.raises(ValueError):
        graph_with_edges.adjacent('Captain Picard', 'Star Wars')
