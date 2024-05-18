class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, val_to_search):
        current_node = self.root
        while current_node is not None:
            if val_to_search == current_node.value:
                return True
            elif val_to_search < current_node.value:
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
        while True:
            if to_insert == current_node.value:
                return False  # Value already exists in the tree
            elif to_insert < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return True
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return True
                current_node = current_node.right

# Example usage
tree = BinarySearchTree()
print(tree.insert(15))  # Output: True (15 inserted)
print(tree.insert(121)) # Output: True (121 inserted)
print(tree.insert(6))   # Output: True (6 inserted)
print(tree.insert(12))  # Output: True (12 inserted)
print(tree.insert(7))   # Output: True (7 inserted)
print(tree.insert(15))  # Output: False (15 already exists)

print(tree.search(15))  # Output: True
print(tree.search(121)) # Output: True
print(tree.search(6))   # Output: True
print(tree.search(12))  # Output: True
print(tree.search(7))   # Output: True
print(tree.search(10))  # Output: False
