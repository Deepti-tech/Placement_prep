class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deep_copy_linked_list(head):
    if not head:
        return None

    # Step 1: Create a mapping to keep track of original nodes and their copies
    node_map = {}

    # Step 2: Traverse the original linked list and create deep copy nodes
    current = head
    while current:
        node_map[current] = Node(current.data)
        current = current.next

    # Step 3: Connect the next pointers of the deep copy nodes based on the mapping
    current = head
    while current:
        if current.next:
            node_map[current].next = node_map[current.next]
        current = current.next

    return node_map[head]

# Example usage:
# Assuming you have a linked list: 1 -> 2 -> 3 -> None
# Create the linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Make a deep copy of the linked list
deep_copy_head = deep_copy_linked_list(head)

# Print the original and deep copied linked lists
print("Original:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

print("Deep Copy:")
current = deep_copy_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
