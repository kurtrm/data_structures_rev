"""Implement a graph depth and breadth traversal."""
from .basic_graph import Graph
from .stack import Stack
from .que_ import Queue

from collections import deque


def depth_first_traversal(graph: Graph, start: 'Node') -> list:
    """Traverse a graph by depth."""
    if not isinstance(graph, Graph):
        raise TypeError('Must provide graph.')
    if not graph.has_node(start):
        raise KeyError('Node not in graph.')
    peeped = set()
    stack = deque()
    stack.append(start)
    while len(stack) > 0:
        node = stack.pop()
        peeped.add(node)
        for neighbor in graph._graph[node]:
            if neighbor not in peeped:
                stack.push(neighbor)
    return peeped


def breadth_first_traversal(graph, start):
    """Traverse a graph by breadth."""
    if not isinstance(graph, Graph):
        raise TypeError('Must provide graph.')
    if not graph.has_node(start):
        raise KeyError('Node not in graph.')
    peeped = []
    queue = Queue()
    queue.enqueue(start)
    while len(queue) > 0:
        node = queue.dequeue()
        if node not in peeped:
            peeped.append(node)
        for neighbor in graph._graph[node]:
            if neighbor not in peeped:
                queue.enqueue(neighbor)
    return peeped


if __name__ == '__main__':
    new_graph = Graph()
    new_graph.add_node('A')
    new_graph.add_node('B')
    new_graph.add_node('C')
    new_graph.add_node('D')
    new_graph.add_node('E')
    new_graph.add_node('F')
    new_graph.add_edge('A', 'B')
    new_graph.add_edge('A', 'C')
    new_graph.add_edge('B', 'D')
    new_graph.add_edge('B', 'E')
    new_graph.add_edge('C', 'B')
    new_graph.add_edge('F', 'A')
    new_graph.add_edge('C', 'F')


    print(new_graph._graph)
    print('depth_first_traversal():')
    print('(A*)->(B*)->(D*)->(B)->(E*)->(B)->(A)->(C*)->(F*)')
    print(depth_first_traversal(new_graph, 'A'))
    print('breadth_first_traversal():')
    print('(A*)->(B*)->(C*)->(D*)->(E*)->(F*)')
    print(breadth_first_traversal(new_graph, 'A'))
