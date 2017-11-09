"""Implement a graph depth and breadth traversal."""
from weighted_graph import Weighted
from stack import Stack
from que_ import Queue


def depth_first_traversal(graph, start):
    """Traverse a graph by depth."""
    if not isinstance(graph, Weighted):
        raise TypeError('Must provide graph.')
    if not graph.has_node(start):
        raise KeyError('Node not in graph.')
    peeped = []
    stack = Stack()
    stack.push(start)
    while len(stack) > 0:
        node = stack.pop()
        if node not in peeped:
            peeped.append(node)
        for neighbor in list(graph[node].keys())[::-1]:
            if neighbor not in peeped:
                stack.push(neighbor)
    return peeped


def breadth_first_traversal(graph, start):
    """Traverse a graph by breadth."""
    if not isinstance(graph, Weighted):
        raise TypeError('Must provide graph.')
    if not graph.has_node(start):
        raise KeyError('Node not in graph.')
    peeped = []
    queue = Queue()
    queue.enqueue(start)
    while queue.size() > 0:
        node = queue.dequeue()
        if node not in peeped:
            peeped.append(node)
        for neighbor in list(graph[node].keys()):
            if neighbor not in peeped:
                queue.enqueue(neighbor)
    return peeped


if __name__ == '__main__':  # pragma no cover
    new_graph = Weighted()
    new_graph.add_node('A')
    new_graph.add_node('B')
    new_graph.add_node('C')
    new_graph.add_node('D')
    new_graph.add_node('E')
    new_graph.add_node('F')
    new_graph.add_edge('A', 'B', 1)
    new_graph.add_edge('A', 'C', 4)
    new_graph.add_edge('B', 'D', 6)
    new_graph.add_edge('B', 'E', 8)
    new_graph.add_edge('C', 'B', 3)
    new_graph.add_edge('F', 'A', 2)
    new_graph.add_edge('C', 'F', 7)

    print(new_graph)
    print('depth_first_traversal():')
    print('(A*)->(B*)->(D*)->(B)->(E*)->(B)->(A)->(C*)->(F*)')
    print(depth_first_traversal(new_graph, 'A'))
    print('breadth_first_traversal():')
    print('(A*)->(B*)->(C*)->(D*)->(E*)->(F*)')
    print(breadth_first_traversal(new_graph, 'A'))
