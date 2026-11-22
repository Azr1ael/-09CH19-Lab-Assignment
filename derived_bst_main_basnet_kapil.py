
# COSC 2436 - Python Programming Assignment 3
# Program Description: Test program for Derived Binary Search Tree
# Name: Kapil Basnet
# Date: 11/22/2026

from derived_bst import Derived_BST


def main():

    # Create a Derived_BST object
    bst = Derived_BST()

    # Insert the required values
    values = [12, 5, 46, 80, 30, 2, 56, 25, 10]

    for value in values:
        bst.insert_node(value)
        print("Node", value, "has been added to the tree")

    # Display maximum and minimum values
    print("Node with max value:", bst.get_max())
    print("Node with min value:", bst.get_min())

    # Insert the additional node
    bst.insert_node(37)
    print("New node 37 has been added to the tree")

    # Test leaf node
    print("Node 37 is a leaf node?", bst.is_leaf(37))

    # Test branch node
    print("Node 37 is a branch?", bst.is_branch(37))

    # Find parent node
    parent = bst.parent_node(37)

    if parent is not None:
        print("Node", parent.key, "is the parent node of node 37")
    else:
        print("Parent node not found")

    # Display total leaf nodes
    print("Total leaf nodes:", bst.total_leaf_nodes(bst.root))

    # Display total non-leaf nodes
    print("Total non-leaf nodes:", bst.total_nonleaf_nodes())

    # Display breadth-first traversal
    print("Breadth-First Traversal:")
    bst.breadth_first()


if __name__ == "__main__":
    main()
