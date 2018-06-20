"""Graph data structure."""


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
        return (key for key in self._graph)

    def edges(self):
        """Return a list of edges in the graph."""
        empty_list = []
        for key, value in self._graph.items():
            if value != []:
                for neighbor in value:
                    empty_list.append((key, neighbor))
        return empty_list

    def add_node(self, val):
        """Add a new node with value to the graph."""
        if val in self._graph.keys():
            raise ValueError("This value is already in your graph.")
        self._graph[val] = []

    def add_edge(self, val1, val2):
        """Add a new edge to the graph."""
        if self._graph.get(val1) is not None and val2 in self._graph.get(val1):
            raise ValueError('This edge already exists.')
        if val1 not in self._graph and val2 not in self._graph:
            self._graph[val1] = []
            self._graph[val2] = []
        elif val1 not in self._graph:
            self._graph[val1] = []
        elif val2 not in self._graph:
            self._graph[val2] = []
        self._graph[val1].append(val2)

    def del_nodes(self, val):
        """Delete the node containing val from list."""
        if val not in self._graph.keys():
            raise ValueError("There is no value to delete.")
        for node in self._graph.values():
            if val in node:
                node.remove(val)
        del self._graph[val]

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






