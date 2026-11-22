
# COSC 2436 - Python Programming Assignment 3
# Program Description: Derived Binary Search Tree
# Name: Kapil Basnet
# Date: 11/22/2026

from bst import BST
from collections import deque


class Derived_BST(BST):

    # Constructor
    def __init__(self):
        super().__init__()

    # Check whether a node is a leaf
    def is_leaf(self, key):
        node = self.search(key)

        if node is None:
            return False

        return node.left is None and node.right is None

    # Check whether a node is a branch
    def is_branch(self, key):
        node = self.search(key)

        if node is None:
            return False

        return node.left is not None or node.right is not None

    # Return the parent node
    def parent_node(self, key):
        if self.root is None or self.root.key == key:
            return None

        parent = None
        current = self.root

        while current is not None:
            if current.key == key:
                return parent

            parent = current

            if key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    # Count total leaf nodes
    def total_leaf_nodes(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return (self.total_leaf_nodes(node.left) +
                self.total_leaf_nodes(node.right))

    # Count total non-leaf nodes
    def total_nonleaf_nodes(self):
        return self.count_nonleaf_nodes(self.root)

    # Helper method for counting non-leaf nodes
    def count_nonleaf_nodes(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 0

        return (1 + self.count_nonleaf_nodes(node.left) +
                self.count_nonleaf_nodes(node.right))

    # Find maximum value
    def get_max(self):
        if self.root is None:
            return None

        current = self.root

        while current.right is not None:
            current = current.right

        return current.key

    # Find minimum value
    def get_min(self):
        if self.root is None:
            return None

        current = self.root

        while current.left is not None:
            current = current.left

        return current.key

    # Breadth-first traversal
    def breadth_first(self):
        if self.root is None:
            return

        queue = deque([self.root])

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                current = queue.popleft()

                print(current.key, end=" ")

                if current.left is not None:
                    queue.append(current.left)

                if current.right is not None:
                    queue.append(current.right)

            print()
