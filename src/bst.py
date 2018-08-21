"""Implement binary search tree."""
from typing import Any, List, Union


class Node:
    """Implement a node of a BST."""

    def __init__(self, val: Any, left: Any=None, right: Any=None, parent: Any=None) -> None:
        """Instantiate a new BST."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class BinTree:
    """Implement a binary search tree."""

    def __init__(self, val: Union[List, tuple, None]=None) -> None:
        """Instantiate a new BST."""
        self._root = None
        self._size = 0
        try:
            for item in val:
                self.insert(item)
        except TypeError:
            if val is not None:
                raise ValueError("Argument must be iterable or None")

    def insert(self, val: Union[int, float]) -> None:
        """Insert a value into a BST iteratively."""
        if not isinstance(val, (int, float)):
            raise ValueError('val argument must be integer or float')

        node = self._root
        try:
            while val != node.val:
                parent = node
                node = node.left if val < node.val else node.right
        except AttributeError:
            if self._root is None:
                self._root = Node(val)
            elif val > parent.val:
                parent.right = Node(val, parent=parent)
            else:
                parent.left = Node(val, parent=parent)
            self._size += 1

    def recursive_insertion(self, val: Union[int, float]) -> None:
        """
        Insert a value into the BST recursively instead of iteratively.
        """
        pass

    def search(self, val: Union[int, float]) -> Union[None, Node]:
        """Search for a value in the BST."""
        if not isinstance(val, (int, float)):
            raise ValueError('val argument must be integer or float')

        node = self._root
        try:
            while val != node.val:
                node = node.left if val < node.val else node.right
            else:
                return node
        except AttributeError:
            pass

    def recursive_search(self, val: Union[int, float]) -> None:
        """
        """
        pass

    def __contains__(self, val: Union[int, float]) -> bool:
        """Check to see if the BST contains a value."""
        return bool(self.search(val))

    @property
    def size(self) -> int:
        """Return the total number of nodes in the BST."""
        return self._size

    def __len__(self) -> int:
        """Return the total number of nodes in the BST."""
        return self._size

    def depth(self, node: Union[None, Node]=None) -> Node:
        """Find the depth of a specified node."""
        if node is None:
            node = self._root
            if node is None:
                return 0

        l_depth = 0
        r_depth = 0

        if node.left:
            l_depth = self.depth(node.left)
        if node.right:
            r_depth = self.depth(node.right)

        if node.left is None and node.right is None:
            return 1
        return l_depth + 1 if l_depth >= r_depth else r_depth + 1

    def balance(self) -> int:
        """Return an integer representing if the tree is balanced or not."""
        start = self._root
        if start is None:
            return 0

        l_depth = 0
        r_depth = 0
        if start.left:
            l_depth = self.depth(start.left)
        if start.right:
            r_depth = self.depth(start.right)
        return l_depth - r_depth

    def delete(self, val: Node) -> None:
        """Delete a given value from the tree and re-order it."""
        start = self.search(val)
        if start:
            is_root = True if start is self._root else False

            if not start.left and not start.right:  # if no children
                if is_root:
                    self._root = None
                else:
                    if start.parent.val > start.val:
                        start.parent.left = None
                    else:
                        start.parent.right = None
            elif start.left and start.right:  # two children
                small = start.left
                is_right = False
                while small.right:
                    small = small.right
                    is_right = True
                start.val = small.val
                if is_right:
                    small.parent.right = small.left
                    if small.left:
                        small.left.parent = small.parent
                else:
                    start.left = small.left
                    if small.left:
                        small.left.parent = start
            elif start.left:
                start.val = start.left.val
                tmp_r = start.left.right
                tmp_l = start.left.left
                start.right = tmp_r
                start.left = tmp_l
            elif start.right:
                start.val = start.right.val
                tmp_r = start.right.right
                tmp_l = start.right.left
                start.right = tmp_r
                start.left = tmp_l
            self._size -= 1
        return None

    def in_order(self, node=None):
        """Traverse the list in order."""
        if node and not isinstance(node, Node):
            raise TypeError('Traversal only accepts None or a Node as params')
        if not node:
            node = self._root
            if not node:
                yield None
        if node.left:
            for each_val in self.in_order(node.left):
                yield each_val
        yield node.val
        if node.right:
            for each_val in self.in_order(node.right):
                yield each_val

    def pre_order(self, node=None):
        """Traverse the list in pre-order."""
        if node and not isinstance(node, Node):
            raise TypeError('Traversal only accepts None or a Node as params')
        if not node:
            node = self._root
            if not node:
                yield None
        yield node.val
        if node.left:
            for each_val in self.pre_order(node.left):
                yield each_val
        if node.right:
            for each_val in self.pre_order(node.right):
                yield each_val

    def post_order(self, node=None):
        """Traverse the list in post-order."""
        if node and not isinstance(node, Node):
            raise TypeError('Traversal only accepts None or a Node as params')
        if not node:
            node = self._root
            if not node:
                yield None
        if node.left:
            for each_val in self.post_order(node.left):
                yield each_val
        if node.right:
            for each_val in self.post_order(node.right):
                yield each_val
        yield node.val

    def breadth_first(self):
        """Perform a BFT on the BST."""
        if not self._root:
            yield None
        yield self._root.val
        traverse = []
        if self._root.left:
            traverse.append(self._root.left)
        if self._root.right:
            traverse.append(self._root.right)
        while traverse:
            curr = traverse[0]
            yield curr.val
            if curr.left:
                traverse.append(curr.left)
            if curr.right:
                traverse.append(curr.right)
            traverse.remove(curr)


if __name__ == '__main__':  # pragma: no cover
    import timeit
    setup = '''
from bst import BinTree
binary_search = BinTree([5, -1, 1, 8, 9, 10, 17, -3, -10, 4, 2, -100, 7, -5, 0, 16, -22, 14, 3, 11])
binary_search.search({})
'''
    pre_bst = [5, -1, 1, 8, 9, 10, 17, -3, -10, 4, 2, -100, 7, -5, 0, 16, -22, 14, 3, 11]
    search_num = input('''
The following values are contained in a binary search tree:
[5, -1, 1, 8, 9, 10, 17, -3, -10, 4, 2, -100, 7, -5, 0, 16, -22, 14, 3, 11]
Enter a number to check the performance of the search function.
>>> ''')
    while isinstance(search_num, str):
        try:
            search_num = int(search_num)
        except ValueError:
            search_num = input("Integer, please.")
    new_setup = setup.format(search_num)
    times = timeit.repeat(new_setup, number=100, repeat=10)
    print('''
Searched binary search tree for the number {} function 100 times, repeated 10 times.
Best: {}s
Worst: {}s'''.format(search_num, min(times), max(times)))