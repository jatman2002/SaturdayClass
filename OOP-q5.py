# Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.

class Node:

    # constructor
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def compare(self, to_compare_with):
        return self.value - to_compare_with


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, val_to_search):
        current_node = self.root

        while (current_node != None):
        
            if current_node.compare(val_to_search) == 0:
                return True

            if current_node.compare(val_to_search) > 0:
                current_node = current_node.left

            if current_node.compare(val_to_search) < 0:
                current_node = current_node.right

        return False

    def insert(self, to_insert):

        root_node = self.root

        while (self.root != None):
        
            if self.root.compare(to_insert) == 0:
                self.root = root_node
                return False

            if self.root.compare(to_insert) > 0:
                self.root = self.root.left

            if self.root.compare(to_insert) < 0:
                self.root = self.root.right

        self.root = Node(to_insert)
        self.root = root_node
        return True


tree = BinarySearchTree()
tree.insert(15)
tree.insert(121)
tree.insert(3)
tree.insert(12)
tree.insert(7)

print()

