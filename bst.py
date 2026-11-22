#BST Tree

class Node:
    """ Represents a single node in the BST."""
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """ Represents the Binary Search Tree."""
    
    def __init__(self):
        self.root = None
        self.size = 0

    def insert_node(self, key):
        """ insert a new key into the BST """
        
        self.root = self.insert_recursive(self.root, key)
        

    def insert_recursive(self, root, key):
        """ helper function to perform the insertion """
        
        if root is None:
            self.size += 1
            return Node(key)
            
        # avoid duplicate
        if key == root.key:
            return root
        if key < root.key:
            root.left = self.insert_recursive(root.left, key)
        else:
            root.right = self.insert_recursive(root.right, key)
        return root

    def search(self, key):
        """ search a node in the tree """
        
        return self.search_recursive(self.root, key)

    def search_recursive(self, root, key):
        """ helper method in the search tree """
        
        if root is None or root.key == key:
            return root
        
        if key > root.key:
            return self.search_recursive(root.right, key)
        
        return self.search_recursive(root.left, key)
    def inorder_traversal(self):
        """ traverse left, root, right """
        
        self.inorder_traversal_recursive(self.root)

    def inorder_traversal_recursive(self, node):
        """ helper function """
        
        if node is None:
            return
    
        # Traverse left subtree
        self.inorder_traversal_recursive(node.left)
    
        # Process current node
        print(f'{node.key}',end=' ' )
        
        # Traverse right subtree
        self.inorder_traversal_recursive(node.right)

    def preorder_traversal(self):
        """ traverse root, left,right """
        
        self.preorder_traversal_recursive(self.root)

    def preorder_traversal_recursive(self, node):
        """ helper function """

        if node is None:
            return
    
        # Process current node
        print(f'{node.key}',end=' ' )
        
        # Traverse left subtree
        self.preorder_traversal_recursive(node.left)
        
        # Traverse right subtree
        self.preorder_traversal_recursive(node.right)
        
    def postorder_traversal(self):
        """ traverse left, right, root """
        
        self.postorder_traversal_recursive(self.root)
    def postorder_traversal_recursive(self, node):
        """ helper function """
        
        if node is None:
            return
        
        # Traverse left subtree
        self.postorder_traversal_recursive(node.left)
        
        # Traverse right subtree
        self.postorder_traversal_recursive(node.right)
        
        # Process current node
        print(f'{node.key}',end=' ' )
        
    def find_min_node(self, node):
        """
        Finds the node with the minimum key in a given subtree.
        This is used to find the in-order successor.
        """
        current_node = node
        # Traverse left until the leftmost node is reached
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
    
    def delete_node(self, key_to_delete):
        """
        Main function to initiate node deletion from the BST.
        It calls the recursive helper function.
        """
        self.root = self.delete_recursive(self.root, key_to_delete)

    def delete_recursive(self, root, key_to_delete):
        """
        Recursively deletes a node with the given key from the BST and returns the new root of the subtree.
        Handles three main cases: leaf node, node with one child, and node with two children.
        """
        # Base Case: If the tree is empty or the node is not found
        if root is None:
            return root

        # Traverse the tree to find the node to be deleted
        if key_to_delete < root.key:
            root.left = self.delete_recursive(root.left, key_to_delete)
        elif key_to_delete > root.key:
            root.right = self.delete_recursive(root.right, key_to_delete)
        else:  # Node with the given key_to_delete is found
            # Case 1: Node has no child (leaf node)
            # Case 2: Node has only one child
            if root.left is None:
                # If there's no left child, replace with the right child (can be None)
                temp_node = root.right
                root = None  # Mark current root for deletion
                return temp_node
            elif root.right is None:
                # If there's no right child, replace with the left child
                temp_node = root.left
                root = None  # Mark current root for deletion
                return temp_node

            # Case 3: Node has two children
            # Get the in-order successor (smallest node in the right subtree)
            successor_node = self.find_min_node(root.right)
            
            # Copy the in-order successor's key to this node
            # This effectively "deletes" the current node by overwriting its key
            root.key = successor_node.key
            
            # Delete the in-order successor from its original position in the right subtree
            root.right = self.delete_recursive(root.right, successor_node.key)
        
        return root
    def get_size(self):
        """ return the size of the tree """
        return self.size
    def path(self, key):
        """ returns a path from the root leading to the specific node """
        lst = []
        current = self.root
        while current != None:
            lst.append(current)
            if key <= current.key:
                current = current.left
            elif key > current.value:
                current = current.right
            else:
                break
    def is_empty(self):
        """ return true if the tree is empty """
        return self.size == 0
    def clear(self):
        """ remove all nodes from the tree """
        self.root = None
        self.size = 0
    def get_root(self):
        """" return the root of the tree """
        return self.root
    

# test BST locally

if __name__ == '__main__':
    
    bst = BST()

    nodes = [50, 30, 20, 40, 70, 60, 80]
    for value in nodes:
        bst.insert_node(value)

    print("\n--- BST Traversal ---")
    print("In-order traversal (expected: 20 30 40 50 60 70 80):")
    bst.inorder_traversal() # Should print 20 30 40 50 60 70 80
    print("\nPre-order traversal (expected: 50 30 20 40 70 60 80):")
    bst.preorder_traversal() # Should print 50 30 20 40 70 60 80
    print("\nPost-order traversal (expected: 20 40 30 60 80 70 50):")
    bst.postorder_traversal() # Should print 20 40 30 60 80 70 50

    print("\n\n--- Searching for elements ---")
    print("Searching for 40:", bst.search(40)) # Expected: True
    print("Searching for 90:", bst.search(90)) # Expected: False
    print("Searching for 50:", bst.search(50)) # Expected: True (root node)

    print("\n--- Deleting elements ---")
    print("Deleting 20 (leaf node)...")
    bst.delete_node(20)
    print("In-order traversal after deleting 20 (expected: 30 40 50 60 70 80):")
    bst.inorder_traversal() # Should print 30 40 50 60 70 80

    print("\nDeleting 70 (node with one child, 80)...")
    bst.delete_node(70)
    print("In-order traversal after deleting 70 (expected: 30 40 50 60 80):")
    bst.inorder_traversal() # Should print 30 40 50 60 80

    print("\nDeleting 50 (node with two children)...")
    bst.delete_node(50)
    print("In-order traversal after deleting 50 (expected: 30 40 60 80):")
    bst.inorder_traversal() # Should print 30 40 60 80

    print("\nAttempting to delete a non-existent node (99)...")
    bst.delete_node(99)
    print("In-order traversal after deleting 99 (should be unchanged):")
    bst.inorder_traversal() # Should print 30 40 60 80
