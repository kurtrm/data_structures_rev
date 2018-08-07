# """Test our depth first and breadth first traversal functions."""
# import pytest


# @pytest.fixture
# def graph():
#     """Graph for our traversals."""
#     from src.basic_graph import Graph
#     new_graph = Graph()
#     new_graph.add_node('A')
#     new_graph.add_node('B')
#     new_graph.add_node('C')
#     new_graph.add_node('D')
#     new_graph.add_node('E')
#     new_graph.add_node('F')
#     new_graph.add_edge('A', 'B')
#     new_graph.add_edge('A', 'C')
#     new_graph.add_edge('B', 'D')
#     new_graph.add_edge('B', 'E')
#     new_graph.add_edge('C', 'B')
#     new_graph.add_edge('F', 'A')
#     new_graph.add_edge('C', 'F')
#     return new_graph


# def test_start_at_a(graph):
#     """Ensure we get a list of stuff starting at a."""
#     from src.graph_traversals_basic import depth_first_traversal
#     assert depth_first_traversal(graph, 'A') == ['A', 'B', 'D', 'E', 'C', 'F']


# def test_only_accepts_graph():
#     """Ensure we can only pass in a graph."""
#     from src.graph_traversals_basic import depth_first_traversal
#     with pytest.raises(TypeError):
#         depth_first_traversal([1, 2, 3])


# def test_only_rejects_nonexistent_node():
#     """Ensure we can't do this with a nonexistent node."""
#     from src.graph_traversals_basic import depth_first_traversal
#     with pytest.raises(TypeError):
#         depth_first_traversal(graph, 'Z')


# def test_start_at_c(graph):
#     """Ensure we get a list of stuff starting at c."""
#     from src.graph_traversals_basic import depth_first_traversal
#     assert depth_first_traversal(graph, 'C') == ['C', 'B', 'D', 'E', 'F', 'A']


# # def test_start_at_a_breadth(graph):
# #     """Ensure we get a list of stuff at a with breadth."""
# #     from src.graph_traversals_basic import breadth_first_traversal
# #     assert breadth_first_traversal(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']


# # def test_start_at_c_breadth(graph):
# #     """Ensure we get a list of stuff starting at c."""
# #     from src.graph_traversals_basic import breadth_first_traversal
# #     assert breadth_first_traversal(graph, 'C') == ['C', 'B', 'F', 'D', 'E', 'A']


# # def test_breadth_only_accepts_graph():
# #     """Ensure we can only pass in a graph."""
# #     from src.graph_traversals_basic import breadth_first_traversal
# #     with pytest.raises(TypeError):
# #         breadth_first_traversal([1, 2, 3])


# # def test_breadth_only_rejects_nonexistent_node():
# #     """Ensure we can't do this with a nonexistent node."""
# #     from src.graph_traversals_basic import breadth_first_traversal
# #     with pytest.raises(TypeError):
# #         breadth_first_traversal(graph, 'Z')
