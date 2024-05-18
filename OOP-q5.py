# Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.

class Node:
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

        while current_node is not None:
            if current_node.compare(val_to_search) == 0:
                return True
            elif current_node.compare(val_to_search) > 0:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    def insert(self, to_insert):
        new_node = Node(to_insert)

        if self.root is None:
            self.root = new_node
            return True

        current_node = self.root
        while current_node is not None:
            if current_node.compare(to_insert) == 0:
                return False  # Duplicate value, do not insert
            elif current_node.compare(to_insert) > 0:
                if current_node.left is None:
                    current_node.left = new_node
                    return True
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return True
                current_node = current_node.right

        return True  # This line should not be reached


tree = BinarySearchTree()
tree.insert(15)
tree.insert(121)
tree.insert(6)
tree.insert(12)
tree.insert(7)

# Example usage
print(tree.search(15))
print(tree.search(121))
print(tree.search(6))
print(tree.search(12))
print(tree.search(7))
print(tree.search(100))  # this will be false
