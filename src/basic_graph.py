"""Directional graph implementation."""


class Graph:
    """A basic implementation of a graph data structure."""
    def __init__(self):
        """Instantiate this graph as a composition of a dictionary."""
        self._graph = {}

    def nodes(self):
        """
        Return a generator of the nodes in the graph.

        Revision:
        This originally returned a list of nodes; however,
        a graph could potentially be huge. Instead, a generator
        of self._graph keys is returned.
        """
        yield from self._graph

    def edges(self):
        """Return a generator of edges in the graph."""
        for key, value in self._graph.items():
            for neighbor in value:
                yield key, neighbor

    def add_node(self, val):
        """Add a new node with value to the graph."""
        self._graph.setdefault(val, set())

    def add_edge(self, val1, val2):
        """Add a new edge to the graph."""
        try:
            self._graph[val1].add(val2)
        except KeyError:
            self._graph[val1] = set()
            self._graph[val1].add(val2)
        self._graph.setdefault(val2, set())

    def del_nodes(self, val):
        """Delete the node containing val from list."""
        try:
            del self._graph[val]
        except KeyError:
            pass

    def del_edges(self, val1, val2):
        """Delete the edge connecting val1 and val2 from the graph."""
        if val2 in self._graph[val1]:
            self._graph[val1].remove(val2)
        else:
            raise ValueError("There are not edges to delete.")

    def has_node(self, val):
        """True is node containing val is in graph, false otherwise."""
        return val in self._graph

    def neighbors(self, val):
        """Return the list of all nodes connected to the node containing val by edges."""
        if val not in self._graph:
            raise ValueError('That value is not in the graph.')
        return self._graph[val]

    def adjacent(self, val1, val2):
        """Return true is val1 and val2 connected, false otherwise."""
        if val1 not in self._graph or val2 not in self._graph:
            raise ValueError("The values are not in the graph.")
        return val2 in self._graph[val1]






