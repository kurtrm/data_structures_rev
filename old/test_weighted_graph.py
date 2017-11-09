"""Test for our weighted graph."""
# {'A': {'B': 7, 'C': 9}, 'B': {'D': 2, 'E': 4}, 'C': {'F':6}}
"""Test our graph implementation."""
import pytest
from weighted_graph import Weighted


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
    new_graph.add_edge('A', 'B', 7)
    new_graph.add_edge('A', 'C', 9)
    new_graph.add_edge('B', 'D', 2)
    new_graph.add_edge('B', 'E', 4)
    new_graph.add_edge('C', 'F', 6)
    return new_graph


def test_graph_init_no_values_taken():
    """Ensure we raise an error if we try to init with a value."""
    from weighted_graph import Weighted
    with pytest.raises(TypeError):
        a_graph = Weighted(2)


def test_graph_init_success(new_weighted_graph):
    """Ensure our new graph is in fact a graph."""
    assert isinstance(new_weighted_graph, Weighted)


def test_graph_adds_and_lists_nodes(graph_no_edges):
    """Ensure we get list of nodes."""
    listy = ['BB', 82, 99, 'AA']
    for node in listy:
        assert node in graph_no_edges.nodes()


def test_graph_adds_nodes_and_edges(graph_no_edges):
    """Ensure we add edges to the nodes."""
    graph_no_edges.add_edge('Louisiana Crawfish', 'WA Invasive Species', 3)
    assert graph_no_edges.edges() == [(
        'Louisiana Crawfish', 'WA Invasive Species', 3)]


def test_graph_lists_adds_and_lists_edges(graph_no_edges):
    """Ensure we add edges to the nodes."""
    graph_no_edges.add_edge(82, 34, 4)
    graph_no_edges.add_edge(99, 'AA', 6)
    assert (82, 34, 4) in graph_no_edges.edges()
    assert (99, 'AA', 6) in graph_no_edges.edges()


def test_graph_deletes_nodes(graph_with_edges):
    """Ensure we can delete a node."""
    graph_with_edges.del_nodes('B')
    listy = ['A', 'C', 'D', 'E', 'F']
    for node in listy:
        assert node in graph_with_edges.nodes()
    assert 'B' not in graph_with_edges.nodes()


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
    graph_with_edges.del_edges('A', 'B')
    assert graph_with_edges['A'] == {'C': 9}


def test_cant_delete_nonexistent_edge(graph_with_edges):
    """Ensure we can't delete a nonexistent edge."""
    with pytest.raises(KeyError):
        graph_with_edges.del_edges('BB', 'Badgers')


def test_nodes_exist(graph_no_edges):
    """Ensure we can assert nodes are in a graph."""
    for node in graph_no_edges:
        assert graph_no_edges.has_node(node)


def test_false_if_no_node(graph_no_edges):
    """Ensure we get false."""
    false_nodes = ['land submarine', 'Portland Timbers', 'tug cable scope', 100]
    for node in false_nodes:
        assert graph_no_edges.has_node(node) is False


def test_node_neighbors(graph_no_edges):
    """Ensure we get the right neighbors for a node."""
    graph_no_edges.add_edge('BB', 82, 5)
    assert graph_no_edges.neighbors('BB') == {82: 5}


def test_node_without_neighbors(graph_no_edges):
    """Ensure we get None back for neighbors."""
    assert graph_no_edges.neighbors(99) == {}


def test_node_error_if_nonpresent(graph_no_edges):
    """Can not get neighbors of nonpresent node."""
    with pytest.raises(ValueError):
        graph_no_edges.adjacent('Raccoon', 'Rocket')


def test_adjacent_nodes(graph_with_edges):
    """Ensure we get adjacent edges."""
    assert graph_with_edges.adjacent('A', 'B')


def test_adjacent_none(graph_with_edges):
    """Ensure we get false."""
    assert graph_with_edges.adjacent('B', 'A') is False


def test_adjacent_unpresent(graph_with_edges):
    """Ensure we get an error."""
    with pytest.raises(ValueError):
        graph_with_edges.adjacent('Captain Picard', 'Star Wars')


def test_add_node_value_error_val_exists(graph_no_edges):
    """Ensure a value is not added twice."""
    with pytest.raises(ValueError):
        graph_no_edges.add_node('BB')


def test_del_edges_has_no_edges_to_delete(graph_with_edges):
    """Ensure there are no edges to delete."""
    with pytest.raises(KeyError):
        graph_with_edges.del_edges('F', 'G')


def test_neighbors_value_error_not_in_graph(graph_with_edges):
        """Ensure the value error raises if no neighbors."""
        with pytest.raises(ValueError):
            graph_with_edges.neighbors('G')


@pytest.fixture
def dijkstra_alg():
    """Test dijkstra method."""
    from weighted_graph import Weighted
    new_graph = Weighted()
    new_graph.add_node('0')
    new_graph.add_node('1')
    new_graph.add_node('2')
    new_graph.add_node('3')
    new_graph.add_node('4')
    new_graph.add_node('5')
    new_graph.add_edge('0', '1', 1)
    new_graph.add_edge('0', '2', 7)
    new_graph.add_edge('1', '3', 9)
    new_graph.add_edge('1', '5', 15)
    new_graph.add_edge('2', '4', 4)
    new_graph.add_edge('3', '5', 5)
    new_graph.add_edge('3', '4', 10)
    new_graph.add_edge('4', '5', 3)
    return new_graph


def test_new_graph_returns_path_to_nodes(dijkstra_alg):
    """Test that the key value pairs are correct."""
    assert dijkstra_alg.dijkstra('0') == {'1': 1, '2': 7, '3': 10, '4': 11, '5': 14}


def test_new_graph_returns_path_to_other_nodes(graph_with_edges):
    """Test that the key value pairs are correct."""
    assert graph_with_edges.dijkstra('A') == {'B': 7, 'C': 9, 'D': 9, 'E': 11, 'F': 15}


def test_graph_with_nodes_pointing_at_each_other():
    """."""
    from weighted_graph import Weighted
    new_weighted = Weighted()
    new_weighted.add_node('A')
    new_weighted.add_node('B')
    new_weighted.add_node('C')
    new_weighted.add_node('D')
    new_weighted.add_node('E')
    new_weighted.add_node('F')
    new_weighted.add_edge('A', 'B', 7)
    new_weighted.add_edge('B', 'C', 9)
    new_weighted.add_edge('B', 'E', 4)
    new_weighted.add_edge('E', 'D', 2)
    new_weighted.add_edge('D', 'C', 2)
    new_weighted.add_edge('C', 'F', 6)
    new_weighted.add_edge('C', 'A', 1)
    assert new_weighted.dijkstra('A') == {'B': 7, 'E': 11, 'D': 13, 'C': 15, 'F': 21}


def test_dijkstra_indext_error_raises(dijkstra_alg):
    """Ensure that index error raises for no node in graph."""
    with pytest.raises(IndexError):
        dijkstra_alg.dijkstra('7')


def test_bellman_ford_first_test_one():
    """Ensure we get same values as dijkstras."""
    from weighted_graph import Weighted
    new_weighted = Weighted()
    new_weighted.add_node('A')
    new_weighted.add_node('B')
    new_weighted.add_node('C')
    new_weighted.add_node('D')
    new_weighted.add_node('E')
    new_weighted.add_node('F')
    new_weighted.add_edge('A', 'B', 7)
    new_weighted.add_edge('B', 'C', 9)
    new_weighted.add_edge('B', 'E', 4)
    new_weighted.add_edge('E', 'D', 2)
    new_weighted.add_edge('D', 'C', 2)
    new_weighted.add_edge('C', 'F', 6)
    new_weighted.add_edge('C', 'A', 1)
    assert new_weighted.bellman_ford('A') == {'A': 0, 'B': 7, 'E': 11, 'D': 13, 'C': 15, 'F': 21}
# {'A': {'B': 7, 'C': 9}, 'B': {'D': 2, 'E': 4}, 'C': {'F': 6}}


def test_bellman_ford_first_test_two(dijkstra_alg):
    """Ensure we get same values as dijkstras."""
    assert dijkstra_alg.bellman_ford('0') == {'0': 0, '1': 1, '2': 7, '3': 10, '4': 11, '5': 14}
# {'A': {'B': 7, 'C': 9}, 'B': {'D': 2, 'E': 4}, 'C': {'F': 6}}


def test_bellman_ford_with_negatives_one():
    """Ensure bellman works with negatives."""
    from weighted_graph import Weighted
    weighted = Weighted()
    weighted.add_node('S')
    weighted.add_node('E')
    weighted.add_node('A')
    weighted.add_node('D')
    weighted.add_node('B')
    weighted.add_node('C')
    weighted.add_edge('S', 'E', 8)
    weighted.add_edge('S', 'A', 10)
    weighted.add_edge('E', 'D', 1)
    weighted.add_edge('D', 'A', -4)
    weighted.add_edge('D', 'C', -1)
    weighted.add_edge('A', 'C', 2)
    weighted.add_edge('C', 'B', -2)
    weighted.add_edge('B', 'A', 1)
    assert weighted.bellman_ford('S') == {'A': 5, 'B': 5, 'C': 7, 'D': 9, 'E': 8, 'S': 0}


def test_bellman_with_negatives_two():
    """Ensure it works with various cases of negatives."""
    from weighted_graph import Weighted
    weighted = Weighted()
    weighted.add_node(0)
    weighted.add_node(1)
    weighted.add_node(2)
    weighted.add_node(3)
    weighted.add_node(4)
    weighted.add_node(5)
    weighted.add_edge(0, 1, 5)
    weighted.add_edge(0, 2, 3)
    weighted.add_edge(1, 3, 7)
    weighted.add_edge(2, 3, -2)
    weighted.add_edge(3, 0, 8)
    weighted.add_edge(3, 4, 3)
    weighted.add_edge(4, 5, 6)
    weighted.add_edge(0, 5, 4)
    assert weighted.bellman_ford(0) == {0: 0, 1: 5, 2: 3, 3: 1, 4: 4, 5: 4}
