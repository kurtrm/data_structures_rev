"""Implement a priority queue using binary heap."""


class PriorityQueue(object):
    """Implement a priority queue."""

    def __init__(self):
        """Initialize our priority queue."""
        self._heap = []
        self._length = 0

    def heapify(self, iterable):
        """Function to heapify our dictionary in self._heap."""
        heap_list = iterable

        def bubble_up(parent, current_node):
            """Helper function to reduce clutter."""
            current_node = parent
            parent = (current_node - 1) // 2
            return (parent, current_node)

        for item in heap_list[::-1]:
            current_node = heap_list.index(item)
            parent = (current_node - 1) // 2
            while current_node > 0:
                parent_priority = list(heap_list[parent].values())[0]
                current_node_priority = list(
                    heap_list[current_node].values())[0]
                if current_node_priority > 0:
                    if parent_priority is 0 or parent_priority > current_node_priority:
                        curr_val = heap_list[parent]
                        heap_list[parent] = heap_list[current_node]
                        heap_list[current_node] = curr_val
                        parent, current_node = bubble_up(parent, current_node)
                    else:
                        parent, current_node = bubble_up(parent, current_node)
                else:
                    parent, current_node = bubble_up(parent, current_node)

        return heap_list

    def insert(self, value, priority=0):
        """Insert a value into the priority queue with an optional priority."""
        if not isinstance(priority, int):
            raise TypeError("Must provide an integer for priority.")
        if priority < 0:
            raise ValueError(
                "You may not use a negative priority."
                "Priority must be 0 or greater.")
        self._heap.append({value: priority})
        if len(self._heap) > 1:
            self._heap = self.heapify(self._heap)
        self._length += 1

    def pop(self):
        """Pop function for removing highest priority item from queue."""
        pop_it = self._heap.pop(0)
        self.heapify(self._heap)
        self._length -= 1
        return list(pop_it.keys())[0]

    def peek(self):
        """Return the highest priority item without removing from queue."""
        return list(self._heap[0].keys())[0]

    def size(self):
        """Return the size of our priority queue."""
        return self._length
