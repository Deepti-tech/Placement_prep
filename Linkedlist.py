class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False


# Utility Functions for Linked List:

def list_to_linked_list(input_list):
    linked_list = LinkedList()
    for item in input_list:
        linked_list.append(item)
    return linked_list

def linked_list_to_list(linked_list):
    output_list = []
    current = linked_list.head
    while current:
        output_list.append(current.data)
        current = current.next
    return output_list

list = LinkedList()
for i in range(5):
    x = int(input())
    list.append(x)
    
list.display()
