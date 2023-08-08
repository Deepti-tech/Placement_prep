class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    def newNode(self, data):
        newnode = Node(data)
        if not self.root:
            self.root = newnode
        else:
            self.insert(self.root, newnode)
    def insert(self, current, newnode):
        if newnode.data < current.data:
            if current.left:
                self.insert(current.left, newnode)
            else:
                current.left = newnode
        else:
            if current.right:
                self.insert(current.right, newnode)
            else:
                current.right = newnode
    def traversal(self):
        return self.inorder_traverse(self.root)
    def inorder_traverse(self, current):
        if not current:
            return []
        left_subtree = self.inorder_traverse(current.left)
        right_subtree = self.inorder_traverse(current.right)        
        return left_subtree + [current.data] + right_subtree
        
          
tree = BinaryTree()
for i in range(5):
    x = int(input())
    tree.newNode(x)
    
print(tree.traversal())

# Utility Functions for Binary Tree:

def list_to_binary_tree(input_list):
    binary_tree = BinaryTree()
    for item in input_list:
        binary_tree.insert(item)
    return binary_tree

def binary_tree_to_list(binary_tree):
    return binary_tree.inorder_traversal()
